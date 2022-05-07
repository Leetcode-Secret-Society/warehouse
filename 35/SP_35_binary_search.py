class Solution:
    def binarySearch(nums: List[int], left: int, right: int, target: int) -> int:
        if left > right: 
            return left
        mid = (left + right) // 2
        if nums[mid] > target:
            return Solution.binarySearch(nums, left, mid-1, target)
        elif nums[mid] < target:
            return Solution.binarySearch(nums, mid+1, right, target)
        else:
            return mid
    def searchInsert(self, nums: List[int], target: int) -> int:
        return Solution.binarySearch(nums, 0, len(nums)-1, target)
