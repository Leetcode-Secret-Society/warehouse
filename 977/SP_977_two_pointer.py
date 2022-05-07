class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        result = []
        for i in range(len(nums)):
            root = 0
            if abs(nums[left]) > abs(nums[right]):
                root = nums[left]
                left += 1
            else:
                root = nums[right]
                right -=1
            result.append(root * root)
        return reversed(result)
                
