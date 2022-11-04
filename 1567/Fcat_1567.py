from typing import List

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        start = 0
        result = 0
        negatives = []
        for i, num in enumerate(nums):
            if num == 0:
                result = max(result, self.check_result(start, i, negatives))
                negatives.clear()
                start = i + 1
            elif num < 0:
                negatives.append(i)
        result = max(result, self.check_result(start, len(nums), negatives))
        return result

    def check_result(self, start, end, negatives):
        if len(negatives) % 2 == 0:
            return end - start
        else:
            return max(end - negatives[0] - 1, negatives[-1] - start, 0)
