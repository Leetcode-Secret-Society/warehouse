from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_length = 0
        left = 0
        zero_count = 0
        for i, num in enumerate(nums):
            print(i, max_length, left)
            if num == 0:
                zero_count += 1
                if zero_count == k+1:
                    max_length = max(i - left, max_length)
                    for next_left in range(left, i+1):
                        if nums[next_left] == 0:
                            left = next_left+1
                            break
                    zero_count -= 1

        max_length = max(len(nums) - left, max_length)
        return max_length