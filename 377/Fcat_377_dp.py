from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def recursive(num):
            if num < 0:
                return 0
            if num in dp:
                return dp[num]
            total = 0
            for n in nums:
                total += recursive(num - n)
            dp[num] = total
            return total
        dp = {}
        nums.sort()
        dp[nums[0]] = 1
        for num in nums[1:]:
            dp[num] = recursive(num)
            dp[num] += 1

        return recursive(target)


print(Solution().combinationSum4([4,2,1], 32))
