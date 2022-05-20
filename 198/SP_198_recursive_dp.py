class Solution:
    def __init__(self):
        self.dp = {}
    def rob(self, nums: List[int]) -> int:
        h_nums = len(nums)
        if h_nums == 0:
            return 0
        if h_nums == 1:
            self.dp[1] = nums[0]
            return self.dp[1]
        if self.dp.get(h_nums) != None:
            return self.dp[h_nums]
        self.dp[h_nums] = max(self.rob(nums[2:]) + nums[0], self.rob(nums[3:]) + nums[1])
        return self.dp[h_nums]
