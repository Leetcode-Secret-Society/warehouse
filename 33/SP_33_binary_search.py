class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def getMin(nums) -> int:
            left = 0
            right = len(nums) - 1
            while nums[left] > nums[right]:
                mid = (left + right) // 2
                # print(f"{left=} {mid=} {right=}")
                if nums[mid] > nums[right]:
                    left = mid + 1
                else: # nums[mid] < right
                    right = mid
                # print(f"{left=} {mid=} {right=}")
            return left
        def binarySearch(nums, target) -> int:
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                # print(mid)
            return -1
        min_pos = getMin(nums)
        
        if target == nums[min_pos]:
            return min_pos
        elif target > nums[-1]:
            correct_nums = nums[:min_pos]
            result = binarySearch(correct_nums,target)
        else:
            correct_nums = nums[min_pos:]
            result = binarySearch(correct_nums,target)
            if result != -1:
                result += min_pos
        return result
