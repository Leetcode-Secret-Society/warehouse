from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        dp = [0] * (amount + 1)
        coins.sort(reverse=True)
        for coin in coins:
            if coin > amount:
                continue
            dp[coin] = 1

        for coin in coins:
            for i in range(coin, amount - coin + 1):
                dp[i+coin] += dp[i]

        return dp[-1]