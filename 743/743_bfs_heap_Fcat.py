from heapq import heappop, heappush
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dict_graph = {}
        for i in range(1, n+1):
            dict_graph[i] = {}

        for start, end, time in times:
            dict_graph[start][end] = time

        shortest_time = {}
        bfs_stack = []
        heappush(bfs_stack, (0, k))
        while bfs_stack:
            time, start = heappop(bfs_stack)
            if start in shortest_time:
                if len(shortest_time) == n:
                    break
                continue
            shortest_time[start] = time
            for node, value in dict_graph[start].items():
                if node not in shortest_time:
                    heappush(bfs_stack, (time + value, node))

        if len(shortest_time) != n:
            return -1

        return max(shortest_time.values())