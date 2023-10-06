class Solution:
    def __init__(self):
        self.dp = {1: 1, 2: 2, 3: 3, 4: 4, 5: 6}

    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n-1
        return self.get_dp(n)

    def get_dp(self, n):
        if n not in self.dp:
            maximum = 0
            for i in range(1, n // 2 + 1):
                maximum = max(self.get_dp(i) * self.get_dp(n - i), maximum)
            self.dp[n] = maximum
        return self.dp[n]
