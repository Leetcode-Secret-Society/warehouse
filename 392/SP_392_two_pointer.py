class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #for t
        s_index = 0
        for t_index in range(len(t)):
            if s_index < len(s) and s[s_index] == t[t_index]:
                s_index += 1
        return s_index == len(s)

        #for s
        t_index = 0
        count = 0
        for s_index in range(len(s)):
            while t_index < len(t):
                if t[t_index] == s[s_index]:
                    count += 1
                    t_index += 1
                    break
                t_index += 1
        return count == len(s)
            
