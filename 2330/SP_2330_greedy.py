#should be easy?
class Solution:
    def makePalindrome(self, s: str) -> bool:
        count = 0
        for i in range(len(s)//2):
            # print(str(i) + ":" + s[i]+' '+s[-i-1])
            if s[i] != s[-i-1]:
                count += 1
            if count > 2:
                return False
        return True
