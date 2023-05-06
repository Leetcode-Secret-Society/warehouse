from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()

        r = len(nums) - 1
        l = 0
        result = 0
        while l < r:
            if nums[r] + nums[l] > target:
                r -= 1
            else:
                result += pow(2, r-l)
                print(result)
                l += 1
        return result % (pow(10, 9) + 7)

