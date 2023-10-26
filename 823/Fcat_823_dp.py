from typing import List


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        factors = [[] for _ in range(len(arr))]
        arr.sort()
        for i, n in enumerate(arr):
            sqrt_n = int(n ** 0.5)
            for j in range(i):
                if arr[j] > sqrt_n:
                    break
                if n % arr[j] == 0:
                    factors[i].append(arr[j])
        dp = {}
        for i, n in enumerate(arr):
            dp[n] = 1
            for factor in factors[i]:
                if n // factor in dp:
                    if factor ** 2 == n:
                        dp[n] += dp[factor] * dp[n // factor]
                    else:
                        dp[n] += dp[factor] * dp[n // factor] * 2

        return sum(dp.values()) % (10 ** 9 + 7)
