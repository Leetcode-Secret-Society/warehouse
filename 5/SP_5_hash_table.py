class Solution:
    def longestPalindrome(self, s: str) -> str:
        pairs = set()
        result = (0,0)
        
        for dist in range(len(s)):
            for i in range(len(s) - dist):
                j = i + dist
                if i == j:                                  #dist=0(self): a
                    pairs.add((i,j))
                elif s[i] == s[j] and i+1 == j:             #dist=1(nearby): aa
                    pairs.add((i,j))
                    result = (i,j)
                elif s[i] == s[j] and (i+1,j-1) in pairs:   #others: aba,abba,ababa
                    pairs.add((i,j))
                    result = (i,j)

        return s[result[0]:result[1]+1]
