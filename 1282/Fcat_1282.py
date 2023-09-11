from collections import defaultdict
from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = defaultdict(list)
        result = []
        for i in range(len(groupSizes)):
            size = groupSizes[i]
            groups[size].append(i)
            if len(groups[size]) == size:
                result.append(groups[size])
                groups[size] = []

        return result