from typing import List
from collections import  defaultdict


class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        max_count = 0
        nums_count = defaultdict(int)
        for num in nums:
            nums_count[num] += 1
            if max_count < nums_count[num]:
                max_count = nums_count[num]

        if max_count <= len(nums) // 2:
            if len(nums) % 2 == 0:
                return 0
            else:
                return 1
        else:
            return 2 * max_count - len(nums)
