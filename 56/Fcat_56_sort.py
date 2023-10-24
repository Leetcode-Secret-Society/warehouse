from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []
        current_interval = intervals[0]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            start, end = interval
            if start > current_interval[1]:
                result.append(current_interval)
                current_interval = interval
            elif end > current_interval[1]:
                current_interval[1] = end
        result.append(current_interval)
        return result