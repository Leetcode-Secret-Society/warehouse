class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        sqrt_n = int(n ** 0.5)
        factors_smaller = []
        factors_larger = []
        for i in range(1,sqrt_n+1):
            if n % i == 0:
                factors_smaller.append(i)
                if i == sqrt_n and sqrt_n ** 2 == n:
                    continue
                factors_larger.append(n//i)
        if k > len(factors_smaller) + len(factors_larger):
            return -1
        elif k <= len(factors_smaller):
            return factors_smaller[k-1]
        else:
            k -= len(factors_smaller)
            return factors_larger[-1*k]