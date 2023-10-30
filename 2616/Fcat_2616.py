from typing import List


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0

        nums.sort()
        gaps = []
        max_gap = 0
        for i in range(len(nums) - 1):
            gap = nums[i + 1] - nums[i]
            gaps.append(gap)
            max_gap = max(max_gap, gap)

        l = 0
        r = max_gap
        while l < r:
            m = (l + r) // 2
            i = 0
            pairs = 0
            while i < len(gaps):
                if gaps[i] <= m:
                    pairs += 1
                    i += 1
                i += 1
            if pairs >= p:
                r = m
            else:
                l = m + 1
        return l
