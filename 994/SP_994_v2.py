class Solution:  
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        fresh = set()
        rotten = deque([])
        rotten_times = 0
        step = 0
        for row in range(r):
            for col in range(c):
                if grid[row][col] == 2:
                    rotten.append((row,col))
                elif grid[row][col] == 1:
                    fresh.add((row,col))
        
        total_flesh = len(fresh)
        if total_flesh == 0:
            return 0
        if len(rotten) == 0:
            return -1
        while rotten:
            if total_flesh == rotten_times:
                return step
            step += 1
            for _ in range(len(rotten)):
                row, col = rotten.popleft()
                for direction in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):
                    if direction in fresh:
                        fresh.remove(direction)
                        rotten.append(direction)
                        rotten_times += 1
            
        return -1
