from typing import List


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        right_sum = sum(nums)
        left_sum = 0
        result = [0] * len(nums)

        for i in range(len(nums)):
            diff_sum = 0
            if i != 0:
                left_sum += nums[i - 1]
                diff_sum += nums[i] * i - left_sum

            right_sum -= nums[i]
            diff_sum += right_sum - (len(nums) - 1 - i) * nums[i]
            result[i] = diff_sum

        return result
