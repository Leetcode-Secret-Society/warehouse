import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        # [1,2,3,4,5]----------------------33
        # 1+2     [3,3,4,5]   3
        # 1+2+3   [6,4,5]     6
        # 1+2+3+4 [10,5]      10      [6,9] 9
        # 1+2+3+4+5   [15]    15      [15] 15
        #                     34           33
        self.heap = []
        for stick in sticks:
            heapq.heappush(self.heap, stick)
        # print(stick)
        curr = heapq.heappop(self.heap)
        result = 0
        while len(self.heap) > 0:
            to_connect = heapq.heappop(self.heap)
            if curr > to_connect:
                heapq.heappush(self.heap, curr)
                curr = heapq.heappop(self.heap)
            curr += to_connect
            result += curr
            # print(f"{curr=} {to_connect=} {result=}")
        return result
