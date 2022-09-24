from typing import List


class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        minimum = len(nums)
        for i in range(len(nums)-1, 1, -1):
            minimum = min(minimum, nums[i])
            if nums[i-2] > minimum:
                return False
        return True
