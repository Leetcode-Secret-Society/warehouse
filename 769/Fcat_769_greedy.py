from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        next_check_num = 0
        checked = [False] * len(arr)
        cur_max_num = 0
        chunk = 0
        for num in arr:
            cur_max_num = max(cur_max_num, num)
            checked[num] = True
            if num == next_check_num:
                for i in range(cur_max_num):
                    if not checked[i]:
                        next_check_num = i
                        break
                else:
                    next_check_num = cur_max_num + 1
                    chunk += 1
        return chunk