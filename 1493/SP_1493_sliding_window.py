#almost the same with 1004
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero_count = 0
        one_count = 0
        j = 0
        result = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                one_count += 1
            else :
                zero_count += 1
            
            while zero_count > 1 and j <= i:
                if nums[j] == 1:
                    one_count -= 1
                else :
                    zero_count -= 1
                j += 1
            result = max(result, one_count + zero_count - 1)
        
        return result
