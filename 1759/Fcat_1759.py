class Solution:
    def countHomogenous(self, s: str) -> int:
        count = 0
        current_c = None
        result = 0
        for c in s:
            if c != current_c:
                result += (count + 1) * count // 2
                current_c = c
                count = 0
            count += 1
        result += (count + 1) * count // 2
        return result % (10 ** 9 + 7)
