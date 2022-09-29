from collections import defaultdict
from typing import List


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        num_count = defaultdict(int)
        for num in arr:
            num_count[num] += 1
        num_list = list(num_count.keys())
        num_list.sort()
        result = 0
        for i in range(len(num_list)-2):
            j = i + 1
            k = len(num_list) - 1
            cur_target = target - num_list[i]
            while j < k:
                if num_list[j] + num_list[k] == cur_target:
                    result += num_count[num_list[i]] * num_count[num_list[j]] * num_count[num_list[k]]
                    j += 1
                    continue
                elif num_list[j] + num_list[k] < cur_target:
                    j += 1
                else:
                    k -= 1
        for i in range(len(num_list)):
            for j in range(i+1, len(num_list)):
                if num_list[i]*2 + num_list[j] == target:
                    result += num_count[num_list[i]] * (num_count[num_list[i]]-1) * num_count[num_list[j]] // 2
                    break
                elif num_list[i] + num_list[j]*2 == target:
                    result += num_count[num_list[i]] * (num_count[num_list[j]]-1) * num_count[num_list[j]] // 2
        for i in range(len(num_list)):
            if num_list[i]*3 == target:
                result += num_count[num_list[i]] * (num_count[num_list[i]]-1) * (num_count[num_list[i]]-2) // 6
                break

        return result % (pow(10,9) + 7)

print(Solution().threeSumMulti(arr = [2,1,3], target = 6))