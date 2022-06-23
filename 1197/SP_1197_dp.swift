class Solution {
    func minKnightMoves(_ x: Int, _ y: Int) -> Int {
        var cache = [String:Int]()
        func dp(_ x: Int,_ y: Int ) -> Int {
            if let cached = cache["\(x):\(y)"] {
                return cached
            }
            if x == 0, y == 0 {
                return 0
            }
            if x + y == 2 {
                return 2
            }
            let result = min(dp(abs(x-1), abs(y-2)), dp(abs(x-2), abs(y-1))) + 1
            cache["\(x):\(y)"] = result
            // cache["\(y):\(x)"] = result
            return result
        }
        return dp(abs(x), abs(y))
    }
}
