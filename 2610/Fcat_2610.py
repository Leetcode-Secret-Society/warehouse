from typing import List
from collections import Counter


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums_2d = []
        num_count = Counter(nums)
        for element, count in num_count.items():
            for i in range(count):
                if len(nums_2d) == i:
                    nums_2d.append([element])
                else:
                    nums_2d[i].append(element)

        return nums_2d
