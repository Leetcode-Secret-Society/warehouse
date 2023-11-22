from typing import List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        max_length = 0
        same_sum_groups = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if i + j == len(same_sum_groups):
                    same_sum_groups.append([nums[i][j]])
                else:
                    same_sum_groups[i + j].append(nums[i][j])

        result = []
        for same_sum in same_sum_groups:
            for i in range(len(same_sum) - 1, -1, -1):
                result.append(same_sum[i])
        return result
