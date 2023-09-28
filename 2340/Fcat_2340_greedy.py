from typing import List

class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        minimum = [float("inf"),0]
        maximum = [0,0]
        for i in range(len(nums)):
            if nums[i] < minimum[0]:
                minimum = [nums[i], i]
            if nums[i] >= maximum[0]:
                maximum = [nums[i], i]

        result = 0
        result += len(nums) - maximum[1] - 1
        result += minimum[1]
        if maximum[1] < minimum[1]:
            result -= 1

        return result
