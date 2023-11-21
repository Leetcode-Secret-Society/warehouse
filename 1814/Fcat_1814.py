from typing import List
from collections import defaultdict


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        result = 0
        nice_num_map = defaultdict(int)
        for num in nums:
            nice_num = num - int(str(num)[::-1])
            result += nice_num_map[nice_num]
            nice_num_map[nice_num] += 1
        return result % (10 **9 + 7)




