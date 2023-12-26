from functools import cache


class Solution:

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        @cache
        def get_roll_ways(n: int, k: int, target: int):
            if target < 0:
                return 0
            elif target == 0:
                if n == 0:
                    return 1
                if n > 0:
                    return 0
            else:
                if n == 0:
                    return 0
            num_rolls = 0
            for point in range(k, 0, -1):
                num_rolls += get_roll_ways(n - 1, k, target - point)
            return num_rolls % (10 ** 9 + 7)

        return get_roll_ways(n, k, target)
