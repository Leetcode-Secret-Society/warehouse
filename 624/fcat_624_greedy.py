from typing import List

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        maximum = arrays[0][-1]
        minimum = arrays[0][0]
        result = 0
        for i in range(1, len(arrays)):
            result = max(result, arrays[i][-1] - minimum, maximum - arrays[i][0])
            maximum = max(maximum, arrays[i][-1])
            minimum = min(minimum, arrays[i][0])
        return result

print(Solution().maxDistance([[-6,-3,-1,1,2,2,2],[-10,-8,-6,-2,4],[-2],[-8,-4,-3,-3,-2,-1,1,2,3],[-8,-6,-5,-4,-2,-2,2,4]]))