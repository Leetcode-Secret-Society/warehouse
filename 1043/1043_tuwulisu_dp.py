class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = []
        l = len(arr)
        for i in range(k):
            dp.append(max(arr[:i+1])*(i+1))
        for i in range(k, l):
            possible = []
            for j in range(k):
                possible.append(dp[i-j-1]+max(arr[i-j:i+1])*(j+1))
            dp.append(max(possible))
        print(dp)
        return dp[-1]
