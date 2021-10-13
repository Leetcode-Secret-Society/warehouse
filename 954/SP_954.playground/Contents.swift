
class Solution {
    func canReorderDoubled(_ arr: [Int]) -> Bool {
        let sorted = arr.sorted()
        var toMatch = [Int]()
        
        var oops = false
        for value in sorted {
            guard let toMatchValue = toMatch.first else {
                toMatch.append(value)
                continue
            }
            if value > 0 {
                let doubledToMatch = toMatchValue * 2
                if (doubledToMatch == value) {
                    toMatch.removeFirst()
                }
                else if (doubledToMatch < value) {
                    oops = true
                    break
                }
                else {
                    toMatch.append(value)
                }
            } else {
                let doubledValue = value * 2
                if (toMatchValue == doubledValue) {
                    toMatch.removeFirst()
                }
                else if (doubledValue > value) {
                    oops = true
                    break
                }
                else {
                    toMatch.append(value)
                }
            }
            
        }
        return oops == false && toMatch.count == 0
    }
}
//Solution().canReorderDoubled([-5,-2])
Solution().canReorderDoubled([-1,-1,-2,-5,1,1,2,2])
//Solution().canReorderDoubled([-1,4,6,8,-4,6,-6,3,-2,3,-3,-8])
//Solution().canReorderDoubled([1,2,4,8])
//Solution().canReorderDoubled([1,2,3,5,9,10])

