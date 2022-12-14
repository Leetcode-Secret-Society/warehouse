class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dic = defaultdict(lambda:0)
        for y in range(len(board)): 
            for x in range(len(board[y])):
                value = board[y][x]
                if value == ".":
                    continue
                x_value = str(y)+"-y="+str(value)
                y_value = str(x)+"-x="+str(value)
                square_value = "square"+str(x//3)+"-"+str(y//3)+"="+str(value)
                if dic[x_value] > 0 or dic[y_value] > 0 or dic[square_value] > 0:
                    return False
                dic[x_value] += 1
                dic[y_value] += 1
                dic[square_value] += 1
        return True
