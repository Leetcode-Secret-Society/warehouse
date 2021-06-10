from typing import List

class Solution:

    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        max_value = nums[0]
        stack = [(0, nums[0])]
        result = [-1] * len(nums)
        for i in range(1, len(nums)):
            current_num = nums[i]
            max_value = max(current_num, max_value)
            while stack and current_num > stack[-1][1]:
                result_i, _ = stack.pop()
                result[result_i] = current_num
            stack.append((i, current_num))

        j = 0
        while j < len(nums) and stack[-1][1] != max_value:
            current_num = nums[j]
            while stack and current_num > stack[-1][1]:
                result_i, _ = stack.pop()
                result[result_i] = current_num
            j += 1

        return result

print(Solution().nextGreaterElements([1,2,3,4,4]))