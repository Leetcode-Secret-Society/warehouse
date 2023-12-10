from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        max_num_indexes = [-1]
        for i in range(len(nums)):
            if nums[i] == max_num:
                max_num_indexes.append(i)
        max_num_indexes.append(len(nums))
        result = 0
        for i in range(1, len(max_num_indexes) - k):
            result += (max_num_indexes[i] - max_num_indexes[i - 1]) * (max_num_indexes[-1] - max_num_indexes[i + k - 1])
        return result
