from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        cur_max = -1
        digit_max = {}
        for num in nums:
            digit_sum = 0
            for digit in str(num):
                digit_sum += int(digit)
            if digit_sum in digit_max:
                cur_max = max(cur_max, digit_max[digit_sum] + num)
                digit_max[digit_sum] = max(digit_max[digit_sum], num)
            else:
                digit_max[digit_sum] = num
        return cur_max
