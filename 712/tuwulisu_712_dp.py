class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = [[None for _ in range(len(s2))] for _ in range(len(s1))]
        for i in range(len(s1)):
            for j in range(len(s2)):
                equal_count = ord(s1[i])+ord(s2[j]) if s1[i]==s2[j] else 0
                if i==0 and j==0:
                    dp[i][j] = equal_count
                elif i==0:
                    dp[i][j] = max(equal_count, dp[i][j-1])
                elif j==0:
                    dp[i][j] = max(equal_count, dp[i-1][j])
                else:
                    dp[i][j] = max(dp[i-1][j-1]+equal_count, dp[i-1][j], dp[i][j-1])
        sum_of_s1 = sum([ord(c) for c in s1])
        sum_of_s2 = sum([ord(c) for c in s2])
        return sum_of_s1+sum_of_s2-dp[len(s1)-1][len(s2)-1]
