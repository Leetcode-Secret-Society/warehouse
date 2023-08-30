class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if s1 == "":
            return s2 == s3
        if s2 == "":
            return s1 == s3
        if len(s1) + len(s2) != len(s3):
            return False

        s2_memo = [True] * (len(s2) + 1)
        for j in range(1, len(s2)+1):
            s2_memo[j] = s2_memo[j-1] and s3[j-1] == s2[j-1]
        print(s2_memo)
        for i in range(len(s1)):
            for j in range(len(s2)+1):
                if j == 0:
                    s2_memo[0] = s2_memo[0] and s1[i] == s3[i]
                    continue
                s2_memo[j] = (s2_memo[j-1] and s2[j-1] == s3[i+j]) or (s2_memo[j] and s1[i] == s3[i+j])
            print(s1[i], s2_memo)

        return s2_memo[-1]

Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac")
