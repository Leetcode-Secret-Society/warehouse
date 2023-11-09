class Solution:
    def countHomogenous(self, s: str) -> int:
        continous = 0
        current_c = None
        result = 0
        for c in s:
            if c != current_c:
                result += (continous + 1) * continous // 2
                current_c = c
                continous = 0
            continous += 1
        result += (continous + 1) * continous // 2
        return result % (10 ** 9 + 7)
