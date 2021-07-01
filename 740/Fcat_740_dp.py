from typing import List
from collections import defaultdict


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        int_count = defaultdict(int)
        for num in nums:
            int_count[num] += 1
        dp = []
        num_keys = sorted(int_count.keys())
        if len(num_keys) == 1:
            return int_count[num_keys[0]] * num_keys[0]
        elif len(num_keys) == 2:
            if num_keys[1] - num_keys[0] == 1:
                return max(int_count[num_keys[1]] * num_keys[1], int_count[num_keys[0]] * num_keys[0])
            else:
                return int_count[num_keys[1]] * num_keys[1] + int_count[num_keys[0]] * num_keys[0]
        else:
            dp.append(int_count[num_keys[0]] * num_keys[0])
            if num_keys[1] - num_keys[0] == 1:
                dp.append(max(int_count[num_keys[1]] * num_keys[1], dp[-1]))
            else:
                dp.append(int_count[num_keys[1]] * num_keys[1] + dp[-1])
            for i in range(2, len(num_keys)):
                cur_earn = int_count[num_keys[i]] * num_keys[i]
                if num_keys[i] - num_keys[i-1] == 1:
                    if num_keys[i-1] - num_keys[i-2] == 1:
                        dp.append(max(dp[-1], dp[-2] + cur_earn))
                    else:
                        dp.append(dp[-2] + max(int_count[num_keys[i-1]] * num_keys[i-1], cur_earn))
                else:
                    dp.append(max(dp[-1], dp[-2]) + cur_earn)

        return dp[-1]


print(Solution().deleteAndEarn([4,10,10,8,1,4,10,9,7,6]))