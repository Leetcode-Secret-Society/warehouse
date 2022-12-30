# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        row, col = binaryMatrix.dimensions()
        result = -1
        current_col_index = col-1
        for y in range(0,row):
            for x in range(current_col_index,-1,-1):
                value = binaryMatrix.get(y,x)
                if value == 0:
                    break
                current_col_index = x
                result = x
        return result
