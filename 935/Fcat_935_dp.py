class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        last_dp = [1, 1, 1, 1, 1, 0, 1, 1, 1, 1]
        for i in range(1, n):
            temp = last_dp[:]
            last_dp[0] = temp[4] + temp[6]
            last_dp[1] = temp[6] + temp[8]
            last_dp[2] = temp[7] + temp[9]
            last_dp[3] = temp[4] + temp[8]
            last_dp[4] = temp[0] + temp[3] + temp[9]
            last_dp[6] = temp[0] + temp[1] + temp[7]
            last_dp[7] = temp[2] + temp[6]
            last_dp[8] = temp[1] + temp[3]
            last_dp[9] = temp[2] + temp[4]

        return sum(last_dp) % (10 ** 9 + 7)
