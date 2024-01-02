import bisect
from collections import deque
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        index = bisect.bisect_left(arr, x)
        result = deque()
        left = index - 1
        right = index
        while len(result) < k:
            if left < 0:
                result.append(arr[right])
                right += 1
            elif right >= len(arr):
                result.appendleft(arr[left])
                left -= 1
            else:
                if x - arr[left] <= arr[right] - x:
                    result.appendleft(arr[left])
                    left -= 1
                else:
                    result.append(arr[right])
                    right += 1

        return list(result)
