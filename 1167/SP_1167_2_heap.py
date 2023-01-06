import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        cost = 0
        # change sticks into min heap
        heapq.heapify(sticks)
        
        while len(sticks)>1:
            # connect lowest 2 sticks together
            stick1 = heapq.heappop(sticks)
            stick2 = heapq.heappop(sticks)
            cost += (stick1+stick2)
            heapq.heappush(sticks,(stick1+stick2))
        return cost
