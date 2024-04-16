class Solution:
  #like 139, but store path
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = [[] for _ in range(len(s) + 1)]
        dp[0] = [""]

        for i in range(len(s)):
            if len(dp[i]) > 0:
                for word in wordDict:
                    w_len = len(word)
                    if s[i:i+w_len] == word:
                        for dp_item in dp[i]:
                            result = word
                            if len(dp_item) > 0:
                                result = dp_item + " " + word
                            dp[i+w_len].append(result)

        return dp[-1]
