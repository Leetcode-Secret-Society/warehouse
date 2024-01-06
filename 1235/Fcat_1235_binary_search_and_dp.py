from typing import List
from functools import cache


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        job_count = len(startTime)
        jobs = []
        for i in range(job_count):
            jobs.append((startTime[i], endTime[i], profit[i]))

        jobs.sort()
        next_job_index = [job_count] * job_count
        for i in range(job_count):
            left = i
            right = job_count
            end_time = jobs[i][1]
            while left < right:
                mid = (left + right) // 2
                if jobs[mid][0] >= end_time:
                    right = mid
                else:
                    left = mid + 1
            next_job_index[i] = right

        @cache
        def find_max_profit(next_job: int):
            if next_job >= job_count:
                return 0

            return max(jobs[next_job][2] + find_max_profit(next_job_index[next_job]), find_max_profit(next_job + 1))

        return find_max_profit(0)
