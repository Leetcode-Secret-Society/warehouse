from typing import List


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        last_moment = 0
        if left:
            most_left = max(left)
            last_moment = max(last_moment, most_left)
        if right:
            most_right = min(right)
            last_moment = max(last_moment, n - most_right)
        return last_moment

