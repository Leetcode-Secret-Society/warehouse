from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        start_index = 0
        cur_sum = nums[0]
        result = 1

        for i in range(1, len(nums)):
            num = nums[i]
            cur_sum += num
            while cur_sum + k < num * (i - start_index + 1):
                cur_sum -= nums[start_index]
                start_index += 1

            result = max(result, (i - start_index + 1))
        return result
