
class Solution:
    def makePalindrome(self, s: str) -> bool:
        not_equal_count = 0
        len_s = len(s)
        for i in range(len_s//2):
            if s[i] != s[len_s - 1 - i]:
                not_equal_count += 1
                if not_equal_count >= 3:
                    return False
        return True
