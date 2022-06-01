from typing import List

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        result = [0] * (n+1)
        for start, end, seats in bookings:
            result[start - 1] += seats
            result[end] -= seats

        for i in range(1, n):
            result[i] += result[i-1]
        return result[:-1]
print(Solution().corpFlightBookings( bookings = [[1,2,10],[2,2,15]], n = 2))