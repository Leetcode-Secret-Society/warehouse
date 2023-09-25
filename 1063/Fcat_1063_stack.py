from typing import List


class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        stack = []
        result = 0
        for i in range(len(nums)):
            while stack and nums[i] < stack[-1][1]:
                j, _ = stack.pop()
                result += i - j
            stack.append((i,nums[i]))

        while stack:
            j, _ = stack.pop()
            result += len(nums) - j

        return result



print(Solution().validSubarrays([1,4,2,5,3]))

