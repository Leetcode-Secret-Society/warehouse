

class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i = 0
        j = 0
        while i < len(str1) and j < len(str2):
            if (ord(str2[j]) - ord(str1[i])) % 26 <= 1:
                j += 1
            i += 1
        return j == len(str2)
