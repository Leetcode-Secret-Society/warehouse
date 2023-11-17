from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maximum = 0
        for i in range(0, len(nums) // 2):
            maximum = max(maximum, nums[i] + nums[len(nums) - 1 - i])
        return maximum
