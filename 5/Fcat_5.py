class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = s[0]

        for i in range(1, len(s)):
            length = 1
            j = 1
            while i - j >= 0 and i + j < len(s):
                if s[i - j] == s[i + j]:
                    length += 2
                    j += 1
                else:
                    break
            j -= 1
            if length > len(result):
                result = s[i - j:i + j + 1]

        for i in range(0, len(s) - 1):
            if s[i] != s[i + 1]:
                continue
            j = 1
            length = 2
            while i - j >= 0 and i + j + 1 < len(s):
                if s[i - j] == s[i + j + 1]:
                    length += 2
                    j+=1
                else:
                    break
            j -= 1
            if length > len(result):
                result = s[i - j:i + j + 2]
        return result