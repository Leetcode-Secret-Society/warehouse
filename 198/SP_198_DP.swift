class Solution {
    var dp = [Int]()
    func rob(_ nums: [Int]) -> Int {
        for i in 0..<nums.count {
            if i == 0{
                dp.append(nums[i])
            }
            else if i == 1 {
                dp.append(max(nums[i], dp[i-1]))
            }
            else {
                dp.append(max(dp[i-1], dp[i-2] + nums[i]))
            }
        }
        return dp.last!
    }
}
