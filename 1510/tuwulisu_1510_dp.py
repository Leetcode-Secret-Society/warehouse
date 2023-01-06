class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        winning_stone_memo = {0: False, 1: True}
        def try_to_win(n)->bool:
            if n in winning_stone_memo:
                return winning_stone_memo[n]
            for i in range(1, n):
                square = i*i
                if square>n:
                    break
                opponent_winning = try_to_win(n - square)
                if not opponent_winning:
                    winning_stone_memo[n] = True
                    return True
            winning_stone_memo[n] = False
            return False
        return try_to_win(n)
