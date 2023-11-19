from typing import List
from collections import Counter


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        num_count = Counter(nums)
        unique_nums = list(num_count.keys())
        unique_nums.sort()
        result = 0
        prefix_sum = 0
        for i in range(len(unique_nums) - 1, 0, -1):
            prefix_sum += num_count[unique_nums[i]]
            result += prefix_sum
        return result
