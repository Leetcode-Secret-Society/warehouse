class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(nums: List[int], target: int) -> int:
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
            return right
        first_ele_each_row = [row[0] for row in matrix]
        col_index = binarySearch(first_ele_each_row, target)
        row_index = binarySearch(matrix[col_index], target)
        if matrix[col_index][row_index] == target:
            return True
        return False
            
