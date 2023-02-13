class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1):
            if i%2==1:
                if nums[i+1]>nums[i]:
                    nums[i+1], nums[i] = nums[i], nums[i+1]
            else:
                if nums[i+1]<nums[i]:
                    nums[i+1], nums[i] = nums[i], nums[i+1]
