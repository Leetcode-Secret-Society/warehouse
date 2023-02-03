from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        target = len(nums)
        dp = [float("inf")] * target
        dp[0] = 0
        farthest = 0
        for i in range(target):
            cur_steps = dp[i]
            farthest_from_i = i + nums[i]
            if farthest < farthest_from_i:
                for j in range(farthest + 1, min(target,farthest_from_i + 1)):
                    dp[j] = cur_steps + 1
                farthest = farthest_from_i
            if farthest_from_i >= target - 1:
                return dp[-1]
