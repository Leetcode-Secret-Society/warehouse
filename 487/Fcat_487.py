from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        zero_indexes = [-1]
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_indexes.append(i)
        zero_indexes.append(len(nums))
        if len(zero_indexes) <= 3:
            return len(nums)

        max_consecutive_ones = 0
        for i in range(len(zero_indexes)-2):
            max_consecutive_ones = max(max_consecutive_ones, zero_indexes[i+2] - zero_indexes[i] - 1)
        return max_consecutive_ones


