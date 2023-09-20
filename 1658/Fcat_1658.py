from typing import List
from collections import defaultdict


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:

        total = sum(nums)
        if total < x:
            return -1
        elif total == x:
            return len(nums)

        i = j = -1
        cur_sum = 0
        max_length = -1
        while i < len(nums):
            target = total - cur_sum
            if target < x:
                j += 1
                cur_sum -= nums[j]
            else:
                if target == x:
                    max_length = max(max_length, i - j)
                i += 1
                if i < len(nums):
                    cur_sum += nums[i]
        if max_length != -1:
            return len(nums) - max_length
        else:
            return -1

print(Solution().minOperations([5,2,3,1,1], 5))