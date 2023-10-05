from typing import List
import bisect


class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        b = []
        condition1 = set()
        for i in range(len(nums)):
            n = nums[i]
            if bisect.bisect_left(b, n) >= k:
                condition1.add(i)
            bisect.insort_right(b, n)

        condition2 = set()
        b = []
        for i in range(len(nums)-1,-1,-1):
            n = nums[i]
            if bisect.bisect_left(b, n) >= k:
                condition2.add(i)
            bisect.insort_right(b, n)

        return len(condition1.intersection(condition2))

print(Solution().kBigIndices([3,8,4,2,5,3,8,6], 1))