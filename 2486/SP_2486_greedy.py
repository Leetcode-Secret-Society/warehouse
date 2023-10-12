class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        l,r = 0, 0
        for i in range(min(len(s),len(t))):
            print(s[i])
            if s[i] != t[i]:
                break
            l = i
            
        r = l
        for i in range(l,len(s)):
            # print((s[i], t[r]))
            if s[i] == t[r]:
                r += 1
                if r == len(t):
                    break
        # print((l, r))

        return len(t) - r
