from functools import lru_cache
class Solution:
    @lru_cache(maxsize=None)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text1 == text2:
            return len(text1)
        
        for i, i_c in enumerate(text1):
            for j, j_c in enumerate(text2):
                if i_c == j_c:
                    result = max(
                        self.longestCommonSubsequence(text1[i+1:], text2[j+1:]) + 1,
                        self.longestCommonSubsequence(text1[i+1:],text2)
                    )
                    return result
        return 0
