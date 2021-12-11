class Solution {
    func numSquares(_ n: Int) -> Int {
        var dp = Array(repeating: Int.max, count: n + 1) //using dictionary will be extreme slow, wired
        dp[0] = 0
        for i in 1...n {
            let root = Float(i).squareRoot()
            for j in 1...Int(root) {
                dp[i] = min(dp[i], dp[i - j*j] + 1);
            }
        }
        return dp[n]
    }
}

Solution().numSquares(13)
