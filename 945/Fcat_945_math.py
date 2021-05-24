from typing import List
from collections import defaultdict


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        if not nums:
            return 0
        upper = 0
        lower = float('inf')
        num_count = defaultdict(int)
        for num in nums:
            upper = max(num, upper)
            lower = min(num, lower)
            num_count[num] += 1

        left_num = 0
        final_sum = 0
        current_sum = 0
        keys = sorted(num_count.keys())
        start = keys[0]
        for i in range(len(keys)):
            num = keys[i]
            if num - start > left_num:
                final_sum += (start + start + left_num - 1) * left_num // 2
                left_num = 0
                start = num

            left_num += num_count[num]
            current_sum += num * num_count[num]

        final_sum += (start + start + left_num - 1) * left_num // 2

        return final_sum - current_sum

Solution().minIncrementForUnique(nums = [3,2,1,2,1,7,7,7,7])