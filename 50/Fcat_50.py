from functools import cache


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        @cache
        def pow(x, n):
            if n == 1:
                return x
            result = pow(x, n // 2) * pow(x, n // 2)
            if n % 2 == 1:
                result *= x
            return result

        if n < 0:
            x = 1 / x
            n *= -1
        return pow(x, n)
