class Solution {
    func maxProfit(_ prices: [Int], _ fee: Int) -> Int {
        var buyDp = Array(repeating: 0, count: prices.count)
        var sellDp = Array(repeating: 0, count: prices.count)
        buyDp[0] = -prices[0]
        for i in 1..<prices.count {
            sellDp[i] = max(buyDp[i-1] + prices[i] - fee, sellDp[i-1])
            buyDp[i] = max(sellDp[i-1] - prices[i] , buyDp[i-1])
        }
        
        // print(buyDp)
        // print(sellDp)
        return max(buyDp.last! , sellDp.last!)
    }
}
