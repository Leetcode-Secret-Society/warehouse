from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        for i in range(len(nums) - 2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l != r:
                current_sum = nums[i] + nums[l] + nums[r]
                if current_sum == 0:
                    results.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r:
                        if nums[l] == nums[l - 1]:
                            l += 1
                        else:
                            break
                elif current_sum > 0:
                    r -= 1
                else:
                    l += 1

        return results
