class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        x_dic = defaultdict(set)
        y_dic = defaultdict(set)
        square_dic = defaultdict(set)
        for y in range(len(board)): 
            for x in range(len(board[y])):
                value = board[y][x]
                if value == ".":
                    continue
                if value in x_dic[x]:
                    return False
                if value in y_dic[y]:
                    return False
                if value in square_dic[(x//3,y//3)]:
                    return False
                
                x_dic[x].add(value)
                y_dic[y].add(value)
                square_dic[(x//3,y//3)].add(value)
        return True
