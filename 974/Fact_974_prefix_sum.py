from collections import defaultdict
from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum_map = defaultdict(int)
        prefix_sum_map[0] = 1
        cur_sum = 0
        result = 0
        for num in nums:
            cur_sum += num
            result += prefix_sum_map[cur_sum % k]
            prefix_sum_map[cur_sum % k] += 1
        return result
