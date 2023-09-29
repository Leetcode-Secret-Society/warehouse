from typing import List
from collections import defaultdict


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        current_len = 1
        result = 0
        for i in range(len(nums) - 1):
            if nums[i+1] <= nums[i]:
                result += (current_len+1) * current_len // 2
                current_len = 1
            else:
                current_len += 1
        result += (current_len + 1) * current_len // 2
        return result
