from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        elif k == len(s):
            return True
        counts = Counter(s)
        odds = 0
        for count in counts.values():
            if count % 2 == 1:
                odds += 1
        if k >= max(1, odds):
            return True

        return False


print(Solution().canConstruct("aaabbb", k =3))
