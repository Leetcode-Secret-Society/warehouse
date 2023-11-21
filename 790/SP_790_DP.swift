class Solution {
    var dp = [Int:Int]()
    let mod:Int = 1_000_000_007
    func numTilings(_ n: Int) -> Int {
        for i in 0...n {
            // print((i,dp))
            if i == 0 {
                dp[i] = 0
            }
            else if i == 1 {
                dp[i] = 1
            }
            else if i == 2 {
                dp[i] = 2
            }
            else if i == 3 {
                dp[i] = 5
            }
            //see: https://leetcode.com/problems/domino-and-tromino-tiling/solutions/116581/detail-and-explanation-of-o-n-solution-why-dp-n-2-d-n-1-dp-n-3/
            //dp[n]=dp[n-1]+dp[n-2]+ 2*(dp[n-3]+...+d[0])
            //dp[4] = 3,1+1,3+2,2
            //dp[5] = 4,1+1,4+3,2+2,3
            else {
                dp[i] = (2*dp[i-1]! + dp[i-3]!)%mod
            }
        }
        // print(dp)
        return dp[n]!
    }
}
