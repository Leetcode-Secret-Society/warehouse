from typing import List
from functools import cache


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if d > len(jobDifficulty):
            return -1

        max_map = {}

        for i in range(len(jobDifficulty)):
            cur_max = jobDifficulty[i]
            max_map[(i, i)] = cur_max
            for j in range(i + 1, len(jobDifficulty)):
                cur_max = max(cur_max, jobDifficulty[j])
                max_map[(i, j)] = cur_max

        @cache
        def getMinDifficulty(index: int, remain_d: int):
            if remain_d == 1:
                return max_map[(index, len(jobDifficulty) - 1)]
            remain_d -= 1
            result = float("inf")
            for i in range(index + 1, len(jobDifficulty) - remain_d + 1):
                result = min(result, max_map[(index, i - 1)] + getMinDifficulty(i, remain_d))
            return result
