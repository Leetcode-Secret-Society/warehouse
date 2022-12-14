class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        one = 1
        two = 1
        for i in range(1, len(s)):
            cur = 0
            if s[i] != '0':
                cur = one
            two_digits = int(s[i-1:i+1])
            if 10 <= two_digits <= 26:
                cur += two
            two = one
            one = cur

        return one