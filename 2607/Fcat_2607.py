from typing import List


class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        group_size = self.find_greatest_common_divisor(len(arr), k)
        groups = [[] for _ in range(group_size)]
        for i in range(len(arr)):
            groups[i % group_size].append(arr[i])

        return sum([self.find_minimum_operation_in_group(group) for group in groups])

    def find_greatest_common_divisor(self, a, b):
        if a % b == 0:
            return b

        return self.find_greatest_common_divisor(b, a % b)

    def find_minimum_operation_in_group(self, group):
        group.sort()
        med = group[len(group) // 2]
        minimum_moves = 0
        for n in group:
            minimum_moves += abs(n - med)
        return minimum_moves


print(Solution().makeSubKSumEqual([1, 4, 1, 3], 2))
