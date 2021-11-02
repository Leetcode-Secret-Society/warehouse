class Solution {
    func findOriginalArray(_ changed: [Int]) -> [Int] {
        if changed.count % 2 == 1 {
            return []
        }
        var dict = [Int:Int]()
        for value in changed {
            dict[value] = (dict[value] ?? 0) + 1
        }
        var result = [Int]()
        for value in dict.keys.sorted() {
            var valueCount = dict[value] ?? 0
            if value == 0 {
                valueCount /= 2
            }
            
            dict[value] = (dict[value] ?? 0) - valueCount
            dict[value * 2] = (dict[value * 2] ?? 0) - valueCount
            
            if dict[value * 2] ?? 0 < 0 {
                return []
            }
            for _ in 0..<valueCount {
                result.append(value)
            }
            
            if result.count == changed.count/2 {
                return result
            }
        }
        return []
    }
}

Solution().findOriginalArray([1,3,4,2,6,8])
Solution().findOriginalArray([6,3,0,1])
Solution().findOriginalArray([0,0,3])
