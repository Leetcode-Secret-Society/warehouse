class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        profit_per_capital = []
        sorted_capital_profit = [(c, p) for c, p in zip(capital, profits)]
        sorted_capital_profit.sort(key=lambda x: x[0], reverse=True)
        
        while k:
            while sorted_capital_profit and sorted_capital_profit[-1][0]<=w:
                c, p = sorted_capital_profit.pop()
                heapq.heappush(profit_per_capital, -p)
            if not profit_per_capital:
                return w
            p = heapq.heappop(profit_per_capital)
            w-=p
            k-=1
        return w
        
