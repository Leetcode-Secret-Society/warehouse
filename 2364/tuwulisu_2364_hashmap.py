class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        all_possibility = n*(n-1)//2
        ratio_count = defaultdict(int)
        for i, n in enumerate(nums):
            if i-n in ratio_count:
                all_possibility -= ratio_count[i-n]
            ratio_count[i-n]+=1

        return all_possibility
