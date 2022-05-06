class Solution:
    def reverse(nums: List[int], start: int, end: int):
        if end < start:
            return
        diff = end - start
        for i in range(math.ceil(diff/2)):
            nums[start+i], nums[end-i] = nums[end-i], nums[start+i]
        
    def rotate(self, nums: List[int], k: int) -> None:
        if k == 0:
            return
        n = len(nums)
        k %= n
        Solution.reverse(nums,0, n-1)
        Solution.reverse(nums,0, k-1)
        Solution.reverse(nums,k, n-1)
