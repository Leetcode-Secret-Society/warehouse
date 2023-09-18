class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        visited = set()
        heap = [(0, 0, 0)]
        while heap:
            effort, x, y = heapq.heappop(heap) 
            if (x, y) not in visited:
                visited.add((x, y))
                if x == n - 1 and y == m - 1:
                    return effort
                else:
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx = x + dx
                        ny = y + dy
                        if nx >=0 and nx < n and ny >=0 and ny < m:
                            new_effort = max(effort, abs(heights[y][x]-heights[ny][nx]))
                            heapq.heappush(heap, (new_effort, nx, ny))
