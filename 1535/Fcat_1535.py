from typing import List


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr):
            return max(arr)
        q = deque(arr[1:])
        win_times = 0
        cur_champ = arr[0]

        while win_times < k:
            if q[0] < cur_champ:
                win_times += 1
                q.append(q.popleft())
            else:
                q.append(cur_champ)
                cur_champ = q.popleft()
                win_times = 1

        return cur_champ
