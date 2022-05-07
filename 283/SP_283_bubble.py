class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nonZeroIndex = 0
        for index in range(len(nums)):
            if nums[index] != 0:
                nums[index], nums[nonZeroIndex] = nums[nonZeroIndex], nums[index]
                nonZeroIndex += 1
