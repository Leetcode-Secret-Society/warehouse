class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        row_sums = defaultdict(lambda: 0)
        col_sums = defaultdict(lambda: 0)
        result = 0
        for row, row_list in enumerate(picture):
            # print(str(row)+'-'+str(row_list))
            for col, value in enumerate(row_list):
                if value == "B":
                    row_sums[row] += 1
                    col_sums[col] += 1
        for row in range(len(picture)):
            if row_sums[row] == 1:
                for col in range(len(picture[0])):
                    if col_sums[col] == 1 and picture[row][col] == "B":
                        result += 1
        return result
            
                
