class Solution:
    def binary_search(self, arr, upper, lower):
        while upper>=lower:
            mid = (upper+lower)//2
            left_neighbor = arr[mid-1] if mid-1>=lower else -1
            right_neighbor = arr[mid+1] if mid+1<=upper else -1
            if left_neighbor<arr[mid] and right_neighbor<arr[mid]:
                return mid
            elif left_neighbor>arr[mid]:
                upper = mid - 1
            elif right_neighbor>arr[mid]:
                lower = mid + 1
            else:
                print("some point are equal")

    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        for y, row in enumerate(mat):
            x_peak = self.binary_search(row, len(row)-1, 0)
            up = -1 if y==0 else mat[y-1][x_peak]
            down = -1 if y==len(mat)-1 else mat[y+1][x_peak]
            if row[x_peak] > up and row[x_peak] > down:
                return (y, x_peak)
            else:
                col = [row[x_peak] for row in mat]
                y_peak = self.binary_search(col, len(col)-1, 0)
                left = -1 if x_peak == 0 else mat[y_peak][x_peak-1]
                right = -1 if x_peak == len(row) - 1 else mat[y_peak][x_peak+1]
                if mat[y_peak][x_peak]>left and mat[y_peak][x_peak]>right:
                    return (y_peak, x_peak)
        return (-1, -1)
