from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = [[] for i in range(n)]
        for connection in connections:
            start, end = connection
            edges[start].append(connection)
            edges[end].append(connection)
        self.reorder_count = 0

        def dfs(parent, node):
            for connection in edges[node]:
                if parent in connection:
                    continue
                start, end = connection
                if start == node:
                    self.reorder_count += 1
                    dfs(node, end)
                else:
                    dfs(node, start)
        dfs(None, 0)
        return self.reorder_count
