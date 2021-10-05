class Solution {
    func maxScore(_ cardPoints: [Int], _ k: Int) -> Int {
        if k >= cardPoints.count {
            return cardPoints.reduce(0, +)
        }
        var index_start = 0
        var index_end = cardPoints.count - 1 - k
        var removedSum = cardPoints[index_start...index_end].reduce(0, +)
//        print("\(removedSum)-\(index_start)-\(index_end)")
        var dp = removedSum
        for _ in index_end..<cardPoints.count - 1{
            removedSum = removedSum - cardPoints[index_start] + cardPoints[index_end+1]
            index_start += 1
            index_end += 1
            dp = min(dp, removedSum)
//            print("\(removedSum)-\(index_start)-\(index_end)")
        }
        return cardPoints.reduce(0, +) - dp
        /*
         正攻
         var index_start = 0
         var index_end = cardPoints.count - 1
         
        for i in 0..<k {
            let startValue = cardPoints[index_start]
            let endValue = cardPoints[index_end]
            if startValue > endValue {
                index_start += 1 //pick start
                result += startValue
            } else {
                index_end -= 1
                result += endValue
            }
        }
         return result
        */
    }
}

//Solution().maxScore([1,2,3,4,5,6,1], 3) //12
Solution().maxScore([1,79,80,1,1,1,200,1], 3) //202
Solution().maxScore([11,49,100,20,86,29,72], 4) //232,正攻法失敗, 11,49,100,72
