class Solution:
    dp = {1:1, 2:2}
    def climbStairs(self, n: int) -> int:
        if self.dp.get(n) != None:
            return self.dp[n]
        self.dp[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.dp[n]
