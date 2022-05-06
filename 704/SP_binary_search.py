class Solution:
    def binarySearch(nums: List[int], left: int, right: int, target: int) -> int:
        if left > right:
            return -1
        mid = (right + left)//2
        if nums[mid] < target:
            return Solution.binarySearch(nums, mid + 1, right, target)
        elif nums[mid] > target:
            return Solution.binarySearch(nums, left, mid - 1, target)
        return mid
    def search(self, nums: List[int], target: int) -> int:
        return Solution.binarySearch(nums, 0, len(nums) - 1, target)
        high = len(nums) - 1
        low = 0
        mid = 0
        while low <= high :
            mid = low + (high-low)//2
            if target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
            else:
                return mid
        
        return -1
