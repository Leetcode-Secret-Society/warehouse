class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        left_most_index = [-1] * 26
        right_most_index = [-1] * 26
        for i in range(len(s)):
            c = s[i]
            if left_most_index[ord(c) - ord("a")] == -1:
                left_most_index[ord(c) - ord("a")] = i
            right_most_index[ord(c) - ord("a")] = i
        result = 0
        for i in range(26):
            left = left_most_index[i]
            right = right_most_index[i]
            if left == right:
                continue
            counted = set()
            for j in range(left + 1, right):
                if s[j] not in counted:
                    counted.add(s[j])
                    result += 1
        return result
