from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        i = 0
        while i < len(nums):
            if nums[i]-1 == i:
                i += 1
                continue
            if nums[i] != nums[nums[i]-1]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
            else:
                i += 1
        for i in range(len(nums)):
            if i != nums[i] - 1 and nums[i] == nums[nums[i]-1]:
                result.append(nums[i])
        return result


print(Solution().findDuplicates([4,3,2,7,8,2,3,1]))
