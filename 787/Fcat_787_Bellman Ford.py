from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dst_price = [{} for _ in range(n)]
        k += 1
        for s, d, price in flights:
            dst_price[s][d] = price

        cur_costs = [float("inf")] * n
        cur_costs[src] = 0
        for _ in range(k):
            previous_costs = cur_costs
            cur_costs = list(previous_costs)
            cur_costs[src] = 0
            for i in range(n):
                last_cost = previous_costs[i]
                if last_cost == float("inf"):
                    continue
                for d, price in dst_price[i].items():
                    cur_costs[d] = min(cur_costs[d], previous_costs[i] + price)

        return cur_costs[dst] if cur_costs[dst] != float("inf") else -1