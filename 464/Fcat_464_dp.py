# Definition for a binary tree node.

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if (maxChoosableInteger+1) * maxChoosableInteger / 2 < desiredTotal:
            return False
        self.win_map = {}
        return self.check_win([i for i in range(1, maxChoosableInteger+1)], desiredTotal, True)

    def check_win(self, candidates, desiredTotal, win_flag):
        key = tuple(candidates)
        if key in self.win_map:
            return self.win_map[key]

        if max(candidates) >= desiredTotal:
            return win_flag

        for i in range(len(candidates)):
            next_candidates = candidates[:i] + candidates[i+1:]
            result = self.check_win(next_candidates, desiredTotal-candidates[i], not win_flag)
            if result is win_flag:
                self.win_map[key] = win_flag
                return win_flag
        self.win_map[key] = not win_flag
        return not win_flag


print(Solution().canIWin(10, 30))
