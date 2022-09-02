class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        row_len = len(board)
        col_len = len(board[0])
        last_char = ""
        def dfs(curr_board, row, col, curr_index) -> bool:
            if curr_index == -1:
                return True
            if row < 0 or col < 0 or row >= row_len or col >= col_len:
                return False
            temp = board[row][col]
            if word[curr_index] != temp:
                return False
            curr_board[row][col] = "#"
            for direction in directions:
                if dfs(curr_board, row+direction[0], col+direction[1], curr_index - 1):
                    return True
            curr_board[row][col] = temp
            return False
        
        
        for row in range(row_len):
            for col in range(col_len):
                if dfs(board, row, col, len(word) - 1): #must runs on backward or it will TLE, like word(AAAAAAAAAAAAAAAAAAAAAB) in array full with 'A'
                    return True
        return False
