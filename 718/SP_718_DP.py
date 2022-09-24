class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        x,y = len(nums1), len(nums2)
        dp = [[0 for _ in range(y+1)] for _ in range(x+1)] 
        result = 0
        for i in range(1,x+1): #start from 1 to x+1 for preventing dp[i-1][j-1] out of bounds
            for j in range(1,y+1):
                # print(str(i)+","+str(j))
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                result = max(dp[i][j], result)
        return result
        
