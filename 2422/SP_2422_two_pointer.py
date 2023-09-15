class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums_sum = sum(nums)
        left,right = 0, len(nums)-1
        left_sum = nums[left]
        right_sum = nums[right]
        count = 0
        while left < right:
            if left_sum < right_sum:
                left += 1
                left_sum += nums[left]
                count += 1
            elif left_sum > right_sum:
                right -= 1
                right_sum += nums[right]
                count += 1
            else:
                #print("BANG")
                left += 1
                right -= 1
                left_sum += nums[left]
                right_sum += nums[right]
        return count
# 4,3,2,1,2,3,1
# (0,6)
# [4'],3,2,1,2,3',[1]
# 1
# (0,5)
# [4],3',2,1,2',[3,1]
# BANG
# (1,4)
# [4,3'],2,1',[2,3,1] 7-6
# 2
# (1,3)
# [4,3],2'',[1,2,3,1] 7-7
# BANG
# (2,2)
# [4,3,[2],1,2,3,1]
# END

# 1,2,3,1
# (0,3)
# [1],2',3',[1]
# BANG
# (1,2)
# [1,2],[3'',1]
# 1
# (2,2)
# [1,2,[3],1]
# END

