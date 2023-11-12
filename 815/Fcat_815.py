from collections import defaultdict, deque
from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        next_stops = defaultdict(list)

        for route in routes:
            route_set = set(route)
            for stop in route:
                next_stops[stop].append(route_set)

        traversed = set()
        queue = deque()
        queue.append((0, source))
        traversed.add(source)
        while queue:
            buses, cur_stop = queue.popleft()
            if cur_stop == target:
                return buses

            while next_stops[cur_stop]:
                route_set = next_stops[cur_stop].pop()
                for stop in route_set:
                    if stop not in traversed:
                        traversed.add(stop)
                        queue.append((buses + 1, stop))
                route_set.clear()
        return -1
