class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        dic = collections.defaultdict(lambda: 0)
        for num in nums:
            dic[num] += 1
        
        count = 0
        for key in list(dic.keys()):
            k_value = dic[key]
            p_value = dic[k - key]
            count += min(k_value, p_value)
        
        return count // 2
