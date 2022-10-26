from collections import defaultdict
class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        diff = endPos - startPos
        adjust_steps = k - abs(diff)
        if adjust_steps%2!=0 or adjust_steps<0:
            return 0
        if diff<0:
            L=adjust_steps//2+abs(diff)
            R=adjust_steps//2
        else:
            R=adjust_steps//2+abs(diff)
            L=adjust_steps//2
        #print(f"{R=} , {L=}")
        dp=defaultdict(lambda: 1)
        for r in range(1, R+1):
            for l in range(1, L+1):
                dp[(r,l)] = (dp[(r-1, l)]+dp[(r, l-1)]) % (10**9+7)
        return dp[(R, L)]
