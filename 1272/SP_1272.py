class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        result = []
        start, end = toBeRemoved[0], toBeRemoved[1]
        for interval in intervals:
            interval_start, interval_end = interval[0], interval[1]
            #make it into 3 parts 
            #---(L)---Start---(Center)---End---(R)---
            if interval_start < start: #if interval_start in L , end would be 3 possibilities --> L/C/R
                if interval_end <= start:
                    result.append(interval)
                else:
                    result.append([interval_start, start])
                if interval_end > end:
                    result.append([end,interval_end])
            elif interval_start >= end: #if interval_start in R , end would be 1 possibility --> R
                result.append(interval)
            else:
                if interval_end > end: #if interval_start in C , end would be 2 possibilities --> C/R
                    result.append([end, interval_end])
                
        return result
