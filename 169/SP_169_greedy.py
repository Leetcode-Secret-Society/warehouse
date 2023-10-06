class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        peak = None
        count = 0
        for n in nums:
            if count == 0:
                peak = n
                count += 1
            elif peak == n:
                count += 1
            else:
                count -= 1
        
        # if nums.count(peak) * 2 > len(nums):
        #     return peak
        # peak is guaranteed
        return peak
