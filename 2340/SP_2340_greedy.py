class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        min_index, min_value = 0, nums[0]
        result = 0
        for index in range(len(nums)):
            num = nums[index]
            if num < min_value:
                min_value = num
                min_index = index
        result += min_index
        element_to_move = nums.pop(min_index)
        nums.insert(0, element_to_move)
        # print(nums)
        
        max_index, max_value = len(nums) - 1, nums[-1]
        for index in range(len(nums) - 1, -1, -1):
            num = nums[index]
            if num > max_value:
                max_value = num
                max_index = index
        result += len(nums) - 1 - max_index
        # print((min_index,min_value))
        # print((max_index,max_value))
        return result

"""
[5,4,3,2,1] 7
4,5,3,2,1
4,3,5,2,1
4,3,2,5,1
4,3,2,1,5
4

4,3,1,2,5
4,1,3,2,5
1,4,3,2,5
3
======================
[2,5,1,3,4]
2
[1,2,5,3,4]
2
[1,2,3,4,5]
"""

