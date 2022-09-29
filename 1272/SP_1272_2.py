class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        result = []
        start, end = toBeRemoved[0], toBeRemoved[1]
        for interval in intervals:
            interval_start, interval_end = interval[0], interval[1]
            #make it into 3 parts 
            #---(L)---Start---(Center)---End---(R)---
            #would be 4 possible ways
            #  A----A
            #       B--------B
            #                       C--------C
            #                                D-----D
            if interval_start >= end:   #A
                result.append(interval)
            elif interval_end <= start: #D
                result.append(interval)
            else:
                if interval_start < start:
                    result.append([interval_start, start])
                if interval_end > end:
                    result.append([end, interval_end])
                
                
        return result
