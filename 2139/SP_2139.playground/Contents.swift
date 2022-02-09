class Solution {
    func isOdd(_ target: Int) -> Bool {
        return target % 2 == 1
    }
    func minMoves(_ target: Int, _ maxDoubles: Int) -> Int {
        var steps = 0
        var result = target
        var doubleCount = maxDoubles
        while (result > 1) {
            if isOdd(result) {
                result -= 1
            }
            else {
                if doubleCount > 0 {
                    result = result/2
                    doubleCount -= 1
                }
                else {
                    return steps + result - 1
                }
            }
            steps += 1
        }
        return steps
    }
}
