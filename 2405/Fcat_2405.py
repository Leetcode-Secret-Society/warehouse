from typing import List
from collections import defaultdict


class Solution:
    def partitionString(self, s: str) -> int:
        partition_set = set()
        result = 1
        for c in s:
            if c in partition_set:
                partition_set.clear()
                result += 1
            partition_set.add(c)
        return result
