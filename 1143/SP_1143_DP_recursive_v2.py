from functools import lru_cache
class Solution:
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(maxsize=None)
        def lcs_index(index1:int, index2: int) -> int:
            if len(text1) == index1 or len(text2) == index2:
                return 0
            if text1[index1] == text2[index2]:
                return lcs_index(index1+1,index2+1) + 1
            return max(lcs_index(index1+1,index2), lcs_index(index1,index2+1))
        
        return lcs_index(0,0)
