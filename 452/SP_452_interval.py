class Solution:
  #like 435, little difference
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key= lambda x: x[1])
        count = 0
        k = -sys.maxsize - 1

        for xs, xe in points:
            if xs > k:
                k = xe
            else:
                count += 1
        
        return len(points) - count
