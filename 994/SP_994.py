class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        q = deque([])
        next_q = deque([])
        total_flesh = 0
        total_rotten = 0
        step = 0
        step_rotten_count = 0
        for row in range(r):
            for col in range(c):
                if grid[row][col] == 2:
                    next_q.append((row,col))
                elif grid[row][col] == 1:
                    total_flesh += 1
        step_rotten_count = len(next_q)
        
        if total_flesh == 0:
            return 0
        if step_rotten_count == 0:
            return -1
        while next_q:
            print(f"{next_q}")
            q = next_q.copy()
            next_q.clear()
            if total_flesh == total_rotten:
                return step
            step += 1
            while q:
                row, col = q.popleft()
                # print(f"{row=}-{col=}, {step=},{grid=}")
                # print(f"{q=}, {next_q=}")

                if total_flesh == total_rotten:
                    return step

                grid[row][col] = 3
                if row + 1 < r:
                    top = grid[row + 1][col]
                    if top == 1:
                        next_q.append((row + 1, col))
                        grid[row + 1][col] = 2
                        total_rotten += 1
                if row - 1 >= 0:
                    bot = grid[row - 1][col]
                    if bot == 1:
                        next_q.append((row - 1, col))
                        grid[row - 1][col] = 2
                        total_rotten += 1
                if col + 1 < c:
                    right = grid[row][col + 1]
                    if right == 1:
                        next_q.append((row, col + 1))
                        grid[row][col + 1] = 2
                        total_rotten += 1
                if col - 1 >= 0:
                    left = grid[row][col - 1]
                    if left == 1:
                        next_q.append((row, col - 1))
                        grid[row][col - 1] = 2  
                        total_rotten += 1
            
        # print(grid)
        # print(total_flesh)
        # print(total_rotten)
        # print(step)
            
        return -1
