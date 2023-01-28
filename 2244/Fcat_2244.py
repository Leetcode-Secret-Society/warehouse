from collections import Counter
from typing import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counts = Counter(tasks)
        result = 0
        for count in counts.values():
            if count == 1: return -1
            result += count // 3
            if count % 3 != 0:
                result += 1
        return result
