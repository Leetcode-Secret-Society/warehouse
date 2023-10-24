class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if k >= len(nums):
            return len(nums)
        zero_count = 0
        one_count = 0
        result = 0
        j = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                one_count += 1
            else:
                zero_count += 1
            while zero_count > k and j < i:
                if nums[j] == 1:
                    one_count -= 1
                else:
                    zero_count -= 1
                j += 1
            result = max(result, one_count + min(k,zero_count))
        return result
