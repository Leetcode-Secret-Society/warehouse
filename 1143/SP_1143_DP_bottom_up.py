from functools import lru_cache
class Solution:
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j+1])
        return dp[0][0]

"""
abc
efg
    c-g[3][3] = 0
    bc-g[2][3] = max(c-g[3][3],abc-x[2][4]) = 0
    abc-g[1][3] = max(bc-g[2][3],abc-x[1][4]) = 0

    c-fg[3][2] = max(c-g[3][3],x-fg[4][2]) = 0
    bc-fg[2][2] = max(c-fg[3][2],bg-g[2][3]) = 0
    abc-fg[1][2] = max(bc-fg[2][2],abc-g[1][3]) = 0

    c-efg[3][1] = max(x-efg[4][1],c-fg[3][2]) = 0
    bc-efg[2][1] = max(c-efg[3][1].bc-fg[2][2]) = 0
    abc-efg[1][1] = max(bc-efg[2][1],abc-fg[1][2]) = 0

xyz
YZX

    z-X = 0
    yz-X = max(z-X,yz-*) = 0
    xyz-X = (x==X)1 + yz-* = 1

    z-ZX = (z==Z)1 + *-X = 1
    yz-ZX = max(z-ZX,yz-X) = 1
    xyz-ZX = max(yz-ZX,xyz-X) = 1

    z-YZX = max(z-ZX,*-YZX) = 1
    yz-YZX = (y==Y)1 + z-ZX = 2
    xyz-YZX = max(yz-YZX,xyz-ZX) = 2
"""