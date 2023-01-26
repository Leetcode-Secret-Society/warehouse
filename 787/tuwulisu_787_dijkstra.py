class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        flight_dict = defaultdict(list)
        for from_, to, price in flights:
            flight_dict[from_].append((from_, to, price))
        most_stops_on_node = [float('inf') for _ in range(n)]
        heap = [[0, 0, src]]
        most_stops_on_node[src]=0
        #print(flight_dict)
        while heap:
            cost, stops, place = heapq.heappop(heap)
            most_stops_on_node[place]=min(stops, most_stops_on_node[place])
            if place == dst:
                return cost
            for _, to, price in flight_dict[place]:
                if stops<=k and stops<most_stops_on_node[to]:
                    heapq.heappush(heap, (cost+price, stops+1, to))
            #print(heap)

        return -1


