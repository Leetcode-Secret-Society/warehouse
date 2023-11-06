from typing import List


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0
        section = []
        for i in range(len(weights) - 1):
            section.append(weights[i] + weights[i + 1])
        section.sort()
        k -= 1
        return sum(section[-k:]) - sum(section[:k])
