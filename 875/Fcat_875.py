import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        def check_hours(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            return hours

        while l < r:
            m = (l + r) // 2
            if check_hours(m) <= h:
                r = m
            else:
                l = m + 1
        return l
