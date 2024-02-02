from functools import lru_cache
class Solution:
    def divide(self, n: int)-> list:
        if n == 2:
            return [(0, 0)]
        else:
            return [(i, n-2-i) for i in range(((n-2)//2)+1)]

    @lru_cache
    def can_win(self, state: tuple)->bool:
        if len(state) == 0:
            return False
        
        for i, plus_count in enumerate(state):
            for a, b in self.divide(plus_count):
                li = []
                if a >= 2:
                    li.append(a)
                if b >= 2:
                    li.append(b)
                if not self.can_win(state[:i]+tuple(li)+state[i+1:]):
                    return True
        return False


    def canWin(self, currentState: str) -> bool:
        consective_plus = 0
        state = list()
        for c in currentState:
            if c == '+':
                consective_plus+=1
            else:
                if consective_plus not in [0, 1]:
                    state.append(consective_plus)
                consective_plus = 0
        if consective_plus not in [0, 1]:
            state.append(consective_plus)
        return self.can_win(tuple(state))
