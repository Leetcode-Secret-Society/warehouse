# Definition for a binary tree node.
from typing import List
from collections import defaultdict, deque


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        start_map = defaultdict(list)
        self.end = False
        for start, end in tickets:
            start_map[start].append(end)

        for airport in start_map:
            start_map[airport].sort()

        def find_result(airport):
            result.append(airport)
            if len(result) == len(tickets) + 1:
                self.end = True
                return
            for i in range(len(start_map[airport])):
                next_airport = start_map[airport][i]
                start_map[airport] = start_map[airport][:i] + start_map[airport][i+1:]
                find_result(next_airport)
                if self.end:
                    return
                result.pop()
                start_map[airport].insert(i, next_airport)

        self.end = False
        result = []
        find_result("JFK")

        return result

Solution().findItinerary([["JFK","ATL"],["ORD","PHL"],["JFK","ORD"],["PHX","LAX"],["LAX","JFK"],["PHL","ATL"],["ATL","PHX"]])




