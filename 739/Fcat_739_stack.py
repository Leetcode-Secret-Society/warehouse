from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i, temperature in enumerate(temperatures):
            while stack and stack[-1][1] < temperature:
                day_i, _ = stack.pop()
                result[day_i] = i - day_i
            stack.append((i, temperature))
        return result
            
        