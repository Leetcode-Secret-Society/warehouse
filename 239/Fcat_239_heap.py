from typing import List
from heapq import heappop, heappush

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        result = []
        for i in range(k-1):
            heappush(heap, (nums[i] * -1, i))

        for i in range(k-1, len(nums)):
            heappush(heap, (nums[i] * -1, i))
            while heap[0][1] <= i-k:
                heappop(heap)
            result.append(heap[0][0]*-1)
        return result
