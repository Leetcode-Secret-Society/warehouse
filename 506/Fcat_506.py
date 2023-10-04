from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cur_sum = 0
        sum_count = defaultdict(int)
        sum_count[0] = 1
        result = 0
        for n in nums:
            cur_sum += n
            result += sum_count[cur_sum-k]
            sum_count[cur_sum] += 1
        return result
