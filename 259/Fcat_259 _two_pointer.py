from typing import List
from collections import defaultdict


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return 0
        nums.sort()
        result = 0
        for i in range(len(nums)-2):
            result += self.two_sum_smaller(i+1, nums, target - nums[i])

        return result

    def two_sum_smaller(self, start_index, nums, target):
        left = start_index
        right = len(nums) - 1
        result = 0
        while left < right:
            if nums[left] + nums[right] < target:
                result += right - left
                left += 1
            else:
                right -= 1
        return result


print(Solution().threeSumSmaller([3,1,0,-2], 3))