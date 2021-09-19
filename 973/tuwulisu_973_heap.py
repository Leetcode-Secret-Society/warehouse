import heapq
class Solution:
    def cal_length(self,x,y):
        return math.sqrt(x*x+y*y)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        length_points = []
        for point in points:
            x = point[0]
            y = point[1]
            length_points.append((self.cal_length(x,y), point))
        heapq.heapify(length_points) # O(n)
        k_smallest = []
        # O(klogn)
        for _ in range(k):
            k_smallest.append(heapq.heappop(length_points)[1])
                                 
        return k_smallest
        

