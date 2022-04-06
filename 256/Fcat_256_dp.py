from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if len(costs) == 1:
            return min(costs[0])
        dp = []
        dp.append(costs[0])
        for index in range(1, len(costs)):
            temp = []
            cost = costs[index]
            for i in range(3):
                temp.append(cost[i]+min(dp[index-1][(i+1)%3], dp[index-1][(i+2)%3]))
            dp.append(temp)
        return min(dp[-1])
