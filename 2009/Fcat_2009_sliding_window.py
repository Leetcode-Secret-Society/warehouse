from typing import List
from collections import defaultdict


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums.sort()
        j = 1
        longest_block = 0
        counter = defaultdict(int)
        counter[nums[0]] += 1
        duplicate = 0
        for i in range(len(nums)):
            while j < len(nums) and nums[j] < nums[i] + len(nums):
                if counter[nums[j]] >= 1:
                    duplicate += 1
                counter[nums[j]] += 1
                j += 1
            longest_block = max(longest_block, j-i - duplicate)
            if counter[nums[i]] >= 2:
                duplicate -= 1
            counter[nums[i]] -= 1
        return len(nums) - longest_block


print(Solution().minOperations([41,33,29,33,35,26,47,24,18,28]))

