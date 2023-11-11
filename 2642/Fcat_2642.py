from typing import List
from heapq import heappop, heappush


class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.edges = [[] for _ in range(n)]
        self.n = n
        for f, t, c in edges:
            self.edges[f].append((c, t))

    def addEdge(self, edge: List[int]) -> None:
        f, t, c = edge
        self.edges[f].append((c, t))

    def shortestPath(self, node1: int, node2: int) -> int:
        h = [(0, node1)]
        cost_to_node = [float("inf")] * self.n
        while h:
            cur_cost, next_node = heappop(h)
            if cur_cost > cost_to_node[next_node]:
                continue
            cost_to_node[next_node] = cur_cost
            if next_node == node2:
                return cur_cost

            for c, t in self.edges[next_node]:
                heappush(h, (cur_cost + c, t))
        return -1
