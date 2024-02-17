from typing import List
from heapq import heappop, heappush


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        cur_bricks = 0
        gap_heap = []
        for i in range(len(heights) - 1):
            gap = heights[i + 1] - heights[i]
            if gap > 0:
                cur_bricks += gap
                heappush(gap_heap, gap * -1)
                if cur_bricks > bricks:
                    if ladders > 0:
                        cur_bricks += heappop(gap_heap)
                        ladders -= 1
                    else:
                        return i
        return len(heights) - 1
