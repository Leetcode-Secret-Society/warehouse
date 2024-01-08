# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()

        left_most = cols
        for row_index in range(rows):
            if left_most != cols and binaryMatrix.get(row_index, left_most) == 0:
                continue
            left = 0
            right = cols if left_most != -1 else left_most

            while left < right:
                mid = (left + right) // 2
                if binaryMatrix.get(row_index, mid) == 1:
                    right = mid
                else:
                    left = mid + 1
            left_most = min(left_most, right)

        if left_most == cols:
            return -1
        else:
            return left_most
