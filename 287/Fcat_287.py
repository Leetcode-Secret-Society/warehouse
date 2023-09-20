from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        high = len(nums) - 1
        low = 1
        cur = (high + low) // 2
        while high > low:

            total = 0
            for n in nums:
                if n <= cur:
                    total += 1
            if total > cur:
                high = cur
            else:
                low = cur + 1
            cur = (high + low) // 2
        return cur

print(Solution().findDuplicate([1,1,2]))
