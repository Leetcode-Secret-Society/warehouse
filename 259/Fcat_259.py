from typing import List
from collections import defaultdict


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return 0
        left = defaultdict(int)
        left[nums[0]] = 1
        right = defaultdict(int)
        for i in range(2, len(nums)):
            right[nums[i]] += 1
        keys = sorted(right.keys())
        result = 0
        for j in range(1, len(nums)-1):
            num_j = nums[j]
            for num_i, i_num in left.items():
                cur_target = target - num_i - num_j
                k_num = 0
                for num_k in keys:
                    if num_k < cur_target:
                        k_num += right[num_k]
                    else:
                        break
                result += i_num * k_num
            right[nums[j+1]] -= 1
            if right[nums[j+1]] == 0:
                keys.remove(nums[j+1])
            left[num_j] += 1
        return result


print(Solution().threeSumSmaller([-2,0,1,3], 2))