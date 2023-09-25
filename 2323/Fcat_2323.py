import math
from typing import List


class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        jobs.sort()
        workers.sort()
        result = 0
        for i in range(len(workers)):
            result = max(result, math.ceil(jobs[i] / workers[i]))

        return result
