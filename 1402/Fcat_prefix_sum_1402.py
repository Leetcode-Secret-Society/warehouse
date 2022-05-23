from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        total = 0
        result = 0
        for num in satisfaction:
            total += num
            if total > 0:
                result += total
            else:
                break
        return result

print(Solution().maxSatisfaction([-1,-8,0,5,-9]))
