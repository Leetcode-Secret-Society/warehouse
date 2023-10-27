class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_dic = collections.defaultdict(lambda: 0)
        col_dic = collections.defaultdict(lambda: 0)
        for i in range(len(grid)):
            row = []
            col = []
            for j in range(len(grid)):
                row.append(grid[i][j])
                col.append(grid[j][i])
            row_dic[str(row)] += 1
            col_dic[str(col)] += 1

        result = 0
        for key in row_dic.keys():
            result += row_dic[key]*col_dic[key]
        
        return result
