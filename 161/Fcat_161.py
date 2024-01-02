class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        if len_s < len_t:
            len_s, len_t = len_t, len_s
            s, t = t, s
        if len_s - len_t == 1:
            for i in range(len_t):
                if s[i] != t[i]:
                    if s[i + 1:] == t[i:]:
                        return True
                    else:
                        return False
            return True
        elif len_s - len_t == 0:
            for i in range(len_t):
                if s[i] != t[i]:
                    if s[i + 1:] == t[i + 1:]:
                        return True
                    else:
                        return False
            return False
        else:
            return False
