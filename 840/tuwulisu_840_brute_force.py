class Solution:
    def isMagicSquare(self, grid, startX, endX, startY, endY) -> bool:
        diag = 0
        antidiag = 0

        for k in range(endX-startX+1):
            diag += grid[startY+k][endX-k]
            antidiag += grid[startY+k][startX+k]
        #print(diag, antidiag)
        if diag!=antidiag:
            return False

        number_dup_checker = set()

        for y in range(startY, endY+1):
            row = 0
            for x in range(startX, endX+1):
                row += grid[y][x]
                if grid[y][x] not in number_dup_checker and grid[y][x]>=1 and grid[y][x]<=9:
                    number_dup_checker.add(grid[y][x])
                else:
                    return False
            if diag!=row:
                return False
        for x in range(startX, endX+1):
            col = 0
            for y in range(startY, endY+1):
                col += grid[y][x]
            if diag!=col:
                return False
        return True
            

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        for y in range(0, m-2):
            for x in range(0, n-2):
                #print(x,y,":")
                if self.isMagicSquare(grid, x, x+2, y, y+2):
                    count+=1
        return count
