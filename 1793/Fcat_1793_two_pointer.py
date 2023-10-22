from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        minimum = nums[k]
        result = nums[k]

        l = k
        r = k

        while True:
            while l != 0 and minimum <= nums[l - 1]:
                l -= 1
            while r != len(nums) - 1 and minimum <= nums[r + 1]:
                r += 1

            result = max(result, (r - l + 1) * minimum)
            if l == 0 and r == len(nums) - 1:
                break
            if r == len(nums) - 1:
                l -= 1
                minimum = nums[l]
            elif l == 0:
                r += 1
                minimum = nums[r]
            else:
                if nums[l - 1] > nums[r + 1]:
                    l -= 1
                    minimum = nums[l]
                else:
                    r += 1
                    minimum = nums[r]
        return result

print(Solution().maximumScore([6569,9667,3148,7698,1622,2194,793,9041,1670,1872], 5))