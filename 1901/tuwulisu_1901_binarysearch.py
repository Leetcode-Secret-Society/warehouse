class Solution:
    def binary_search(self, mat, upper, lower):
        while upper>=lower:
            mid = (upper+lower)//2
            mid_row_max = max(mat[mid])
            up_row_max = max(mat[mid-1]) if mid-1>=lower else -1
            down_row_max = max(mat[mid+1]) if mid+1<=upper else -1
            if up_row_max<mid_row_max and down_row_max<mid_row_max:
                return [mid, mat[mid].index(mid_row_max)]
            elif up_row_max>mid_row_max:
                upper = mid - 1
            elif down_row_max>=mid_row_max:
                lower = mid + 1

    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        return self.binary_search(mat, len(mat)-1, 0)
        
            
