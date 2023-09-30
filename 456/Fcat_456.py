from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        minimums = [0] * len(nums)
        cur_min = nums[0]

        for i in range(len(nums)):
            cur_min = min(nums[i], cur_min)
            minimums[i] = cur_min

        stack = []
        for j in range(len(nums)-1 ,-1, -1):
            if nums[j] < minimums[j]:
                continue
            while stack and stack[-1] <= minimums[j]:
                stack.pop()
            if stack and stack[-1] < nums[j]:
                return True
            stack.append(nums[j])

        return False


print(Solution().find132pattern([-2,1,-2]))


