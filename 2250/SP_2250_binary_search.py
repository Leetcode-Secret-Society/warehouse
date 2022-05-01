import bisect
from typing import List
class Solution:
    def binarySearch(arr: List[int], x:int) -> int:
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = low + (high-low)//2
            # print(str(arr[low])+"-"+str(arr[mid])+"-"+str(arr[high]))
            if arr[mid] < x:
                low = mid + 1
            elif arr[mid] > x :
                high = mid - 1
            else :
                return mid
        return low

    def getNearbyPos(arr: List[int], x:int) -> int:
        return Solution.binarySearch(arr, x)
        # linear search
        # for (i, value) in enumerate(arr):
        #     if value >= x:
        #         print("value:"+str(value)+"\t\t pos:"+str(i))
        #         return i
        # return len(arr)

    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        dict = {}
        # result = List[int]
        result = list()
        for rect in rectangles:
            x = rect[0]
            y = rect[1]
            if (y in dict) == False:
                dict[y] = [x]
            else :
                dict[y].append(x)
        for k,v in dict.items():
            v.sort()

        # print(dict)

        # keys = sorted(list(dict.keys()))
        # for point in points:
        #     pointResult = 0
        #     x = point[0]
        #     y = point[1]
            
        #     yPos = Solution.getNearbyPos(keys, y)
        #     for i in range(yPos, len(keys)):
                
        #         xArr = dict[keys[i]]
        #         # print("key[y]:"+str(keys[i])+"\txArr="+str(xArr)+"-->"+str(len(xArr) - Solution.getNearbyPos(xArr, x)))
        #         pointResult += len(xArr) - Solution.getNearbyPos(xArr, x)
        #     result.append(pointResult)

        
        for point in points:
            pointResult = 0
            x = point[0]
            y = point[1]
            for i in range(y, 101):
                if i in dict:
                    xArr = dict[i]
                    # print("key[y]:"+str(keys[i])+"\txArr="+str(xArr)+"-->"+str(len(xArr) - Solution.getNearbyPos(xArr, x)))
                    pointResult += len(xArr) - Solution.getNearbyPos(xArr, x)
                    # pointResult += len(xArr) - bisect.bisect_left(xArr, x) #faster
            result.append(pointResult)

        return result

print(Solution().countRectangles(
[[8,4],[10,8],[7,2],[10,5],[4,7],[9,9],[5,2],[1,5]],
[[8,2]]
))
# Solution.binarySearch([1,3,5,7,9],8)