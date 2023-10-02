from typing import List


class Solution:
    def countTheNumOfKFreeSubsets(self, nums: List[int], k: int) -> int:
        group_by_module = [[] for _ in range(k)]
        for n in nums:
            group_by_module[n % k].append(n)
        dp = [0] * 50
        dp[0] = 1
        dp[1] = 2
        group_lengths = []
        for i in range(2, 50):
            dp[i] = dp[i-2] + dp[i-1] + 1

        for g in group_by_module:
            if not g:
                continue
            g.sort()
            group_len = 1
            for j in range(1, len(g)):
                if g[j-1] == g[j] - k:
                    group_len += 1
                else:
                    group_lengths.append(dp[group_len-1])
                    group_len = 1
            group_lengths.append(dp[group_len-1])
        result = 1
        for l in group_lengths:
            result *= (l+1)
        return result


print(Solution().countTheNumOfKFreeSubsets([2,3,5,8], 5))