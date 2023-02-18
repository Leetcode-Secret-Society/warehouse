import math
class Solution:
    def build_kmp_map(self, s):
        t = [0] * len(s)
        t[0] = -1
        i = 1
        cnd = 0
        while i < len(s):
            if s[i]==s[cnd]:
                t[i] = t[cnd]
            else:
                t[i] = cnd
                while cnd>=0 and s[i]!=s[cnd]:
                    cnd = t[cnd]
            i+=1
            cnd+=1
        return t
    def kmp_search(self, t, a, b):
        i = 0
        j = 0
        
        while j<len(a):
            if a[j] == b[i]:
                if i == len(b)-1:
                    return True
            else:
                i = t[i]
                while i>=0 and b[i]!=a[j]:
                    i = t[i]
            i+=1
            j+=1
        
        return False
    def repeatedStringMatch(self, a: str, b: str) -> int:
        
        times = math.ceil(len(b)/len(a))
            
        at = a*times
        t = self.build_kmp_map(b)
        found = self.kmp_search(t, at, b)
        if found:
            return times
        at += a
        found = self.kmp_search(t, at, b)
        if found:
            return times+1
        return -1
