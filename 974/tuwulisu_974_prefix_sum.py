class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int)
        counter[0]=1
        s = 0
        count = 0
        for n in nums:
            s += n
            count+=counter[s%k]
            counter[s%k]+=1
        return count
