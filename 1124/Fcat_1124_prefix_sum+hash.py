from typing import List

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        seen = {}
        temp = 0
        result = 0
        for i, hour in enumerate(hours):
            if hour > 8:
                temp += 1
            else:
                temp -= 1
            if temp > 0:
                result = i+1
            seen.setdefault(temp, i)
            if temp - 1 in seen:
                result = max(i - seen[temp-1], result)

        return result

print(Solution().longestWPI([9,9,6,0,6,6,9]))