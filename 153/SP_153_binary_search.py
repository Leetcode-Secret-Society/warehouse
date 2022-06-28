class Solution:
    def findMin(self, nums: List[int]) -> int:
        # def getMin(nums) -> int:, from search in rotated array
        left = 0
        right = len(nums) - 1
        # print(f"[{left}]{nums[left]=} [{mid}]{nums[mid]=} [{right}]{nums[right]=}")
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else: # nums[mid] < right
                right = mid
            # print(f"[{left}]{nums[left]=} [{mid}]{nums[mid]=} [{right}]{nums[right]=}")
        return nums[left]
