class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: #speed up
            return (-1, -1)
        def binary_search_right() -> int:
            left = 0
            right = len(nums) - 1
            while left < right:
                pivot = ceil((left + right) / 2)
                if nums[pivot] == target:
                    left = pivot
                elif nums[pivot] > target:
                    right = pivot - 1
                else :
                    left = pivot + 1
                # print(f"{pivot=} {nums[pivot]=} {left=} {right=}")
            return right
        def binary_search_left() -> int:
            left = 0
            right = len(nums) - 1
            while left < right :
                pivot = (left + right) // 2
                if nums[pivot] == target:
                    right = pivot
                elif nums[pivot] > target:
                    right = pivot - 1
                else :
                    left = pivot + 1
                # print(f"{pivot=} {nums[pivot]=} {left=} {right=}")
            return left
        result_right = binary_search_right()
        if result_right == -1: #not found
            return (-1, -1)
        if nums[result_right] != target: #not found
            return (-1, -1)
        result_left = binary_search_left()
        return (result_left, result_right)
