from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        l = 0
        r = len(nums)
        # right
        while l < r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m
            else:
                l = m + 1
        right = l - 1
        if nums[right] != target:
            return [-1, -1]
        # left
        l = 0
        while l < r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        left = l

        return [left, right]

Solution().searchRange([1,2,3],2)