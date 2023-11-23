from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = []

        for l_index, r_index in zip(l, r):
            num_set = set()
            minimum = maximum = nums[l_index]
            for i in range(l_index, r_index + 1):
                num_set.add(nums[i])
                maximum = max(maximum, nums[i])
                minimum = min(minimum, nums[i])

            if (maximum - minimum) % (r_index - l_index) != 0:
                result.append(False)
                continue
            diff = (maximum - minimum) // (r_index - l_index)
            start = minimum

            for i in range((r_index - l_index)):
                start += diff
                if start not in num_set:
                    result.append(False)
                    break
            else:
                result.append(True)

        return result

print(Solution().checkArithmeticSubarrays([-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10],[0,1,6,4,8,7],[4,4,9,7,9,10]))