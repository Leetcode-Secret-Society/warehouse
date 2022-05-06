# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def binarySearch(left: int, right: int) -> int:
        if left > right:
            return left
        mid = (left + right) // 2
        if isBadVersion(mid) == False:
            return Solution.binarySearch(mid+1, right)
        else :
            return Solution.binarySearch(left, mid-1)
        
    def firstBadVersion(self, n: int) -> int:
        return Solution.binarySearch(0, n)
        low = 0 
        high = n
        mid = 0
        while low <= high:
            mid = (low + high) // 2
            if isBadVersion(mid) == False:
                low = mid + 1
            else :
                high = mid - 1
        # print(str(low)+"-"+str(mid)+"-"+str(high))
        return low
