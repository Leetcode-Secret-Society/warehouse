class Solution {
    func numSplits(_ s: String) -> Int {
        
        var set = Set<Character>() //using set is faster than dictionary
        var leftLetterCount = [Int]() //using array is faster than dictionary
        var rightLetterCount = [Int]()
        for char in s {
            if set.contains(char) == false {
                set.insert(char)
            }
            leftLetterCount.append(set.count)
        }
        set.removeAll()
        for char in s.reversed() {
            if set.contains(char) == false {
                set.insert(char)
            }
            rightLetterCount.append(set.count)
        }
        rightLetterCount.reverse()
        var result = 0
        for i in 0..<(s.count - 1) {
            let leftValue = leftLetterCount[i]
            let rightValue = rightLetterCount[i+1]
            if leftValue == rightValue {
                result += 1
            }
        }
        return result
    }
}
Solution().numSplits("aacaba")//112233
Solution().numSplits("aaaaa")
