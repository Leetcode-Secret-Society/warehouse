from typing import List

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        largest = [(float('-inf'), -1), (float('-inf'), -1)]
        smallest = [(float('inf'), -1), (float('inf'), -1)]
        for array_index in range(len(arrays)):
            if arrays[array_index][-1] > largest[0][0]:
                largest[1] = largest[0]
                largest[0] = (arrays[array_index][-1], array_index)
            elif arrays[array_index][-1] > largest[1][0]:
                largest[1] = (arrays[array_index][-1], array_index)

            if arrays[array_index][0] < smallest[0][0]:
                smallest[1] = smallest[0]
                smallest[0] = (arrays[array_index][0], array_index)
            elif arrays[array_index][0] < smallest[1][0]:
                smallest[1] = (arrays[array_index][0], array_index)

        if largest[0][1] != smallest[0][1]:
            return largest[0][0] - smallest[0][0]
        else:
            return max(largest[0][0] - smallest[1][0], largest[1][0] - smallest[0][0])

print(Solution().maxDistance([[-3,-2],[-2,-2,-2]]))