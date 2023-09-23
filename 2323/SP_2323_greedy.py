class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        jobs.sort()
        workers.sort()
        result = 0
        for i in range(len(workers)):
            worker = workers[i]
            job = jobs[i]
            result = max(result, math.ceil(job / worker))

        return int(result)
