import math
from typing import List
from collections import defaultdict


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        if k == 1:
            return len(nums) * (len(nums) - 1) // 2
        appeared_factor = defaultdict(int)
        sqrt_k = k ** 0.5
        sqrt_k = int(sqrt_k)
        k_factors = []
        for factor in range(1, sqrt_k + 1):
            if k % factor == 0:
                k_factors.append(factor)
                if k // factor != factor:
                    k_factors.append(k // factor)

        pair_count = 0
        for num in nums:
            remain_factor = k // math.gcd(num, k)
            pair_count += appeared_factor[remain_factor]
            for factor in k_factors:
                if num % factor == 0:
                    appeared_factor[factor] += 1

        return pair_count
