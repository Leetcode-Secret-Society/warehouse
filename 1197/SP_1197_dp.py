class Solution:
    dp = {}
    def minKnightMoves(self, x: int, y: int) -> int:
        abs_x = abs(x)
        abs_y = abs(y)
        if x == 0 and y == 0:
            return 0
        if abs_x == 2 and abs_y == 1:
            return 1
        if abs_x == 1 and abs_y == 2:
            return 1
        if abs_x + abs_y == 2:
            return 2
        if self.dp.get((abs_x,abs_y)):
            return self.dp[(abs_x,abs_y)]
        a = (abs_x - 2, abs_y - 1) #though there might be negitive pos here, but next turn it will be absoluted by line 4,5
        b = (abs_x - 1, abs_y - 2) 
        self.dp[(abs_x,abs_y)] = min(self.minKnightMoves(a[0],a[1]),self.minKnightMoves(b[0],b[1])) + 1
        return self.dp[(abs_x,abs_y)]
        
