from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        i = 0
        j = 1
        cost = 0

        while j < len(colors):
            if colors[i] != colors[j]:
                i = j
                j = i + 1
            else:
                if neededTime[i] < neededTime[j]:
                    cost += neededTime[i]
                    i = j
                    j = i + 1
                else:
                    cost += neededTime[j]
                    j += 1
        return cost
