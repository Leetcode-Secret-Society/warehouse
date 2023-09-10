from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            check_horizontal = [False] * 10
            check_vertical = [False] * 10
            for j in range(9):
                cur_h = board[i][j]
                cur_v = board[j][i]
                if cur_v != '.':
                    if check_vertical[int(cur_v)]:
                        return False
                    check_vertical[int(cur_v)] = True
                if cur_h != '.' :
                    if check_horizontal[int(cur_h)]:
                        return False
                    check_horizontal[int(cur_h)] = True

        for block_i in range(0,9,3):
            for block_j in range(0,9,3):
                check_block = [False] * 10
                for i in range(3):
                    for j in range(3):
                        cur = board[block_i+i][block_j+j]
                        if cur == '.':
                            continue
                        if check_block[int(cur)]:
                            return False
                        check_block[int(cur)] = True
        return True

Solution().isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])