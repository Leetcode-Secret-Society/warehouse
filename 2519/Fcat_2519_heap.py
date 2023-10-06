from typing import List
from heapq import heappop, heappush

class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        h = []
        condition1 = [False] * len(nums)
        condition2 = [False] * len(nums)
        for i in range(len(nums)):
            if len(h) == k:
                if h[0] * -1 < nums[i]:
                    condition1[i] = True
                else:
                    heappop(h)
                    heappush(h, nums[i] * -1)
            else:
                heappush(h, nums[i] * -1)

        h = []
        for i in range(len(nums)-1,-1,-1):
            if len(h) == k:
                if h[0] * -1 < nums[i]:
                    condition2[i] = True
                else:
                    heappop(h)
                    heappush(h, nums[i] * -1)
            else:
                heappush(h, nums[i] * -1)
        result = 0
        for i in range(len(nums)):
            if condition1[i] and condition2[i]:
                result += 1

        return result

print(Solution().kBigIndices([3,8,4,2,5,3,8,6], 1))