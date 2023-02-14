class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        queue = [(start[0], start[1], 0)]
        visited = defaultdict(lambda: float('inf'))
        visited[tuple(start)] = 0
        min_dis = float('inf')
        while queue:
            new_queue = []
            for y, x, distance in queue:
                for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    yd = y + direction[0]
                    xd = x + direction[1]
                    dis = 0
                    while (yd>=0 and yd<m and xd>=0 and xd<n) and maze[yd][xd]==0:
                        yd += direction[0]
                        xd += direction[1]
                        dis+=1
                    yd -= direction[0]
                    xd -= direction[1]
                    if yd==destination[0] and xd == destination[1]:
                        min_dis = min(distance+dis, min_dis)
                        break
                    if dis+distance<visited[(yd, xd)]:
                        visited[(yd, xd)] = dis+distance
                        new_queue.append((yd, xd, dis+distance))
            
            queue = new_queue
        if min_dis != float('inf'):
            return min_dis
        else:
            return -1
