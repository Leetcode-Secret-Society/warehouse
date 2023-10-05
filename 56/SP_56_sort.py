class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key =lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged: #initial
                merged.append(interval)
            else: 
                #
                # 1---3
                #   2-----6
                #   2---4
                #     3--5
                if interval[0] <= merged[-1][-1]: 
                    merged[-1][-1] = max(merged[-1][-1], interval[1])
                else:
                    merged.append(interval)
        return merged
