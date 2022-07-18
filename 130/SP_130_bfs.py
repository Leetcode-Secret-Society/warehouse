class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        max_row, max_col = len(board), len(board[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        area = set()
        visited = set()
        to_go_set = set()
        def bfs(start_row, start_col):
            to_go_set.add((start_row, start_col))
            while len(to_go_set) > 0:
                (row, col) = to_go_set.pop()
                if (row, col) not in visited:
                    visited.add((row, col))
                    if board[row][col] == "O":
                        area.add((row, col))
                        for direction in directions:
                            to_go = (row + direction[0], col + direction[1])
                            if to_go[0] < 0 or to_go[0] >= max_row or to_go[1] < 0 or to_go[1] >= max_col:
                                pass
                            else :
                                to_go_set.add((to_go[0], to_go[1]))
        

        for row in range(max_row):
            for col in [0, max_col - 1]:
                if board[row][col] == "O":
                    bfs(row, col)
                    for item in area:
                        board[item[0]][item[1]] = "E"
                    area.clear()
        
        for row in [0, max_row -1]:
            for col in range(max_col):
                if board[row][col] == "O":
                    bfs(row, col)
                    for item in area:
                        board[item[0]][item[1]] = "E"
                    area.clear()
        
        for row in range(max_row):
            for col in range(max_col):
                if board[row][col] == "E":
                    board[row][col] = "O"
                elif board[row][col] == "O":
                    board[row][col] = "X"
