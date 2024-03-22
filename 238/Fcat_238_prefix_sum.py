from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left = [nums[0]] * len(nums)
        right = [nums[-1]] * len(nums)
        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i]
            right[-1 * i - 1] = right[-1 * i] * nums[-1 * i - 1]

        result = [0] * len(nums)
        result[0] = right[1]
        result[-1] = left[-2]

        for i in range(1, len(nums) - 1):
            result[i] = left[i - 1] * right[i + 1]

        return result
