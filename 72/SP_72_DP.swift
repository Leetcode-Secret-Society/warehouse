class Solution {
    func minDistance(_ word1: String, _ word2: String) -> Int {
        if word1 == word2 { return 0 }
        var dp = Array(repeating: Array(repeating: ("-",0), count: word2.count+1), count: word1.count+1)
        var word1 = Array(word1)
        var word2 = Array(word2)
        //in case word1 or word2 are empty
        for i in 1..<word1.count + 1{ 
            dp[i][0] = ("\(word1[i-1])-_",i)
        }
        for j in 1..<word2.count + 1{
            dp[0][j] = ("_-\(word2[j-1])",j)
        }
        for i in 1..<word1.count + 1{
            for j in 1..<word2.count + 1{
                // print((i,j))
                if word1[i-1] == word2[j-1] {
                    dp[i][j] = ( "\(word1[i-1])-\(word2[j-1])", dp[i-1][j-1].1)
                }
                else {
                    dp[i][j] = ( "\(word1[i-1])-\(word2[j-1])",min(dp[i-1][j-1].1, dp[i-1][j].1, dp[i][j-1].1) + 1)
                }
            }
        }
        // for item in dp {
        //     print(item)
        // }
        return dp[word1.count][word2.count].1
    }
}
