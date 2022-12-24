from pprint import pprint
class Solution:
    def singleLongestPalindrome(self, word) -> list:
        word_length = len(word)
        dp = [[1 if i==j else 0 for j in range(word_length)] for i in range(word_length)]
        for length in range(2, word_length+1):
            for i in range(word_length-(length-1)):
                j = i + length - 1
                if word[i]==word[j]:
                    dp[i][j] = max(dp[i+1][j-1]+2, dp[i+1][j], dp[i][j-1])
                else:
                    dp[i][j] = max(dp[i+1][j-1], dp[i+1][j], dp[i][j-1])
        return dp
    def longestPalindrome(self, word1: str, word2: str) -> int:
        len1 = len(word1)
        len2 = len(word2)
        word1_dp = self.singleLongestPalindrome(word1)
        word2_dp = self.singleLongestPalindrome(word2)
        """for i in range(len2):
            for j in range(len2):
                print((i,j),word2_dp[i][j], end=', ')
            print("")"""

        dp = [[0 for _ in word2] for _ in word1]

        dp[len1-1][0] = 2 if word1[len1-1] == word2[0] else 0
        i = len1 - 1
        for j in range(1, len2):
            if word1[i] == word2[j]:
                dp[i][j] = 2 + word2_dp[0][j-1]
            else:
                dp[i][j] = dp[i][j-1]
        
        j = 0
        for i in range(len1-2, -1, -1):
            if word1[i] == word2[j]:
                dp[i][j] = 2 + word1_dp[i+1][len1-1]
            else:
                dp[i][j] = dp[i+1][j]

        for i in range(len1-2, -1, -1):
            for j in range(1,len2):
                if word1[i] == word2[j]:
                    dp[i][j] = max(dp[i+1][j-1]+2, dp[i][j-1], dp[i+1][j], word1_dp[i+1][len1-1]+2, word2_dp[0][j-1]+2)
                else:
                    dp[i][j] = max(dp[i+1][j-1], dp[i][j-1], dp[i+1][j])
        """for i in range(len1):
            for j in range(len2):
                print((i,j),dp[i][j], end=', ')
            print("")"""
        return dp[0][len2-1]
