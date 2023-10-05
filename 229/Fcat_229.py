from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1 = count2 = 0
        candidates = [None, None]
        for n in nums:
            if n == candidates[0]:
                count1 += 1
            elif n == candidates[1]:
                count2 += 1
            elif count1 == 0:
                candidates[0] = n
                count1 += 1
            elif count2 == 0:
                candidates[1] = n
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1

        for i in range(1, -1, -1):
            if candidates[i] is None or nums.count(candidates[i]) <= len(nums) // 3:
                candidates.pop(i)
        return candidates