class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      # must write an algorithm that runs in O(n) time and without using the division operation.
      # 3n
        from_left = [0] * len(nums)
        from_left[0] = nums[0]
        from_right = [0] * len(nums)
        from_right[-1] = nums[-1]
        result = [0] * len(nums)
        for i in range(1,len(nums)):
            from_left[i] = from_left[i-1] * nums[i]
            from_right[-i-1] = from_right[-i] * nums[-i-1]

        for i in range(1,len(nums)-1):
            result[i] = from_left[i-1] * from_right[i+1]
        result[0] = from_right[1] 
        result[-1] = from_left[-2]
        return result
