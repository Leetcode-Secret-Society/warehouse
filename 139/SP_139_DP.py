class Solution:
  #buttom up
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s)):
            if dp[i] == True:
                for word in wordDict:
                    w_len = len(word)
                    if s[i:i+w_len] == word:
                        dp[i+w_len] = True
        
        return dp[-1]
