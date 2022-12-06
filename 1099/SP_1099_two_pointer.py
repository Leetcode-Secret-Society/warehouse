class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        sorted_nums = sorted(nums)
        print(sorted_nums)
        left, right = 0, len(nums) - 1
        result = -1
        while left < right:
            left_val, right_val = sorted_nums[left], sorted_nums[right]
            if left_val + right_val >= k:
                right -= 1
            else :
                result = max(left_val + right_val, result)
                left += 1

        return result
