from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        max_num = 0
        patched = 0
        index = 0
        while max_num < n:
            if index < len(nums) and nums[index] <= max_num + 1:
                max_num += nums[index]
                index += 1
            else:
                max_num += max_num + 1
                patched += 1

        return patched