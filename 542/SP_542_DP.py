class Solution:
    def updateMatrixX(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        for r in range(m):
            for c in range(n):
                if mat[r][c] > 0:
                    top = mat[r - 1][c] if r > 0 else math.inf
                    left = mat[r][c - 1] if c > 0 else math.inf
                    mat[r][c] = min(top, left) + 1
        print(mat)

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if mat[r][c] > 0:
                    bottom = mat[r + 1][c] if r < m - 1 else math.inf
                    right = mat[r][c + 1] if c < n - 1 else math.inf
                    mat[r][c] = min(mat[r][c], bottom + 1, right + 1)
        print(mat)
        return mat
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        height = len(mat)
        width = len(mat[0])
        for row_index in range(height):
            for col_index in range(width):
                if mat[row_index][col_index] != 0:
                    nearby_distance = [math.inf]

                    if col_index - 1 >= 0:
                        nearby_distance.append(mat[row_index][col_index - 1])
                    if row_index - 1 >= 0:
                        nearby_distance.append(mat[row_index - 1][col_index])

                    result = min(nearby_distance)
                    # print(f"{row_index=}-{col_index=}-{result=}")
                
                    mat[row_index][col_index] = result + 1
        # print(mat)
        for row_index in range(height -1, -1, -1):
            for col_index in range(width -1, -1, -1):
                if mat[row_index][col_index] != 0:
                    nearby_distance = [math.inf]

                    if col_index + 1 < width:
                        nearby_distance.append(mat[row_index][col_index + 1])
                    if row_index + 1 < height:
                        nearby_distance.append(mat[row_index + 1][col_index])

                    result = min(nearby_distance)
                    # print(f"{row_index=}-{col_index=}-{result=}")
                    
                    # compare with previous(top left) record
                    mat[row_index][col_index] = min(mat[row_index][col_index], result + 1)
                    
        # print(mat)
        return mat
