from typing import List


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        profit_difficulty = {}

        for i in range(len(profit)):
            profit_difficulty[profit[i]] = min(difficulty[i], profit_difficulty.get(profit[i], difficulty[i]))

        sorted_profit = list(profit_difficulty.keys())
        sorted_profit.sort(reverse=True)
        max_profit = 0
        worker.sort(reverse=True)
        i = 0
        for w in worker:
            while i < len(sorted_profit):
                if profit_difficulty[sorted_profit[i]] <= w:
                    max_profit += sorted_profit[i]
                    break
                i += 1
        return max_profit

Solution().maxProfitAssignment(difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7])