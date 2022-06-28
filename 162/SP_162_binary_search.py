class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #from 33.Search in Rotated Sorted Array
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2
        # print(f"[{left}]{nums[left]=} [{mid}]{nums[mid]=} [{right}]{nums[right]=}")
        while left < right:
            mid = (left + right) // 2
            nearby_value = nums
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else: # nums[mid] < right
                right = mid
            # print(f"[{left}]{nums[left]=} [{mid}]{nums[mid]=} [{right}]{nums[right]=}")
        return right
