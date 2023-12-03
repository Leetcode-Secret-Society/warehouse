from typing import List


class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        max_obtainable = 0
        index = 0
        added = 0
        while max_obtainable < target:
            if index < len(coins) and coins[index] <= max_obtainable + 1:
                max_obtainable += coins[index]
                index += 1
            else:
                max_obtainable += max_obtainable + 1
                added += 1
        return added
