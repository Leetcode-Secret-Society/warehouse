import math
from typing import List


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        touchdown = [0] * len(dist)
        for i in range(len(dist)):
            touchdown[i] = math.ceil(dist[i] / speed[i])

        touchdown.sort()
        eliminate = 0

        for i in range(len(touchdown)):
            if i >= touchdown[eliminate]:
                break

            eliminate += 1

        return eliminate