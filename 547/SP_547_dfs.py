class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        #copied from 200, but enumerate all children ele, and no need boundary
        def dfs(row, col) :
            if isConnected[row][col] == 0:
                return
            isConnected[row][col] = 0
            isConnected[col][row] = 0
            for col_col in range(len(isConnected[col])):
                dfs(col, col_col)
        result = 0
        for row in range(len(isConnected)):
            for col in range(len(isConnected[row])):
                val = isConnected[row][col]
                if val == 1:
                    result += 1
                    dfs(row , col)
        return result
