from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        left = [len(arr)] * len(arr)
        right = [-1] * len(arr)
        stack = []
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                left[stack.pop()] = i
            stack.append(i)
        stack.clear()
        for i in range(len(arr) - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                right[stack.pop()] = i
            stack.append(i)
        result = 0
        for i in range(len(arr)):
            result += arr[i] * (i - left[i]) * (right[i] - i)
        return result % (pow(10, 9) + 7)
