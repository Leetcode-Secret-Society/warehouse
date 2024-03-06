class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        for j in range(len(obstacleGrid)):
            for i in range(len(obstacleGrid[j])):
                if obstacleGrid[j][i] == 0:
                    if i == 0 and j == 0:
                        dp[j][i] = 1
                    elif i == 0:
                        dp[j][i] = dp[j-1][i]
                    elif j == 0:
                        dp[j][i] = dp[j][i-1]
                    else:
                        dp[j][i] = dp[j-1][i] + dp[j][i-1]
                # print(f"{i}-{j}={dp[j][i]}")
                # print(obstacleGrid[j][i])
        return dp[-1][-1]
