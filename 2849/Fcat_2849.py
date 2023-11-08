class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        larger_dist = max(abs(sx - fx), abs(sy - fy))
        if t == 1 and sx == fx and sy == fy:
            return False

        if t < larger_dist:
            return False

        return True
