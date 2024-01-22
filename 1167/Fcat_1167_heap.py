from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapify(sticks)
        cost = 0
        while len(sticks) >= 2:
            new_stick = heappop(sticks) + heappop(sticks)
            cost += new_stick
            heappush(sticks, new_stick)
        return cost
