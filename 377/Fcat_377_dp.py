from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def recursive(num):
            if num < 0:
                return 0
            if num == 0:
                return 1
            if num in dp:
                return dp[num]
            total = 0
            for n in nums:
                total += recursive(num - n)
            dp[num] = total
            return total

        dp = {}
        return recursive(target)


print(Solution().combinationSum4([4, 2, 1], 32))
