from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closet = float("inf")
        result = 0
        for i in range(len(nums) - 2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l != r:
                current_sum = nums[i] + nums[l] + nums[r]
                if abs(current_sum - target) < closet:
                    closet = abs(current_sum - target)
                    result = current_sum
                elif current_sum - target > 0:
                    r -= 1
                else:
                    l += 1

        return result

print(Solution().threeSumClosest([-1,2,1,-4], 1))
