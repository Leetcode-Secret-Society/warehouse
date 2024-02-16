from collections import Counter
from typing import List


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        num_counts = list(counter.values())
        num_counts.sort()
        for i in range(len(num_counts)):
            if k < num_counts[i]:
                return len(num_counts) - i
            k -= num_counts[i]

        return 0
