from functools import cache


class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        if len(s) - k <= 1:
            return True

        @cache
        def check_is_palindrome(left: int, right: int, k: int) -> bool:
            if left >= right:
                return True
            if s[left] != s[right]:
                if k == 0:
                    return False
                return check_is_palindrome(left + 1, right, k - 1) or check_is_palindrome(left, right - 1, k - 1)
            else:
                return check_is_palindrome(left + 1, right - 1, k)

        return check_is_palindrome(0, len(s) - 1, k)
