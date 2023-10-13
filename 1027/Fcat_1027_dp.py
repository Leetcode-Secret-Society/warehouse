from typing import List
from collections import defaultdict


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        dp = []
        longest = 0
        for i in range(len(nums)):
            cur_dp = defaultdict(int)
            for j in range(i):
                cur_dp[nums[i] - nums[j]] = dp[j][nums[i] - nums[j]] + 1
                longest = max(longest, cur_dp[nums[i] - nums[j]])
            dp.append(cur_dp)
        return longest + 1

print(Solution().longestArithSeqLength([20,1,15,3,10,5,8]))