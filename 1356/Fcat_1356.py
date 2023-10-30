from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        results = [[] for _ in range(15)]
        for num in arr:
            one_nums = bin(num).count('1')
            results[one_nums].append(num)

        result = []
        for r in results:
            r.sort()
            result.extend(r)
        return result

