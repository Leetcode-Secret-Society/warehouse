class Solution {
    func findReplaceString(_ s: String, _ indices: [Int], _ sources: [String], _ targets: [String]) -> String {
        var resultArr = Array<String>()
        for c in s {
            resultArr.append("\(c)")
        }
        let start = s.startIndex
        let end = s.endIndex
        for (i, index) in indices.enumerated() {
            let offset = s.index(start, offsetBy: index)
            let source = sources[i]
            let target = targets[i]
            if s[offset..<end].starts(with: source) {
                resultArr[index] = target
                for j in index+1..<index+source.count {
    //                print(j)
                    resultArr[j] = ""
                }
            }
        }
//        print(resultArr)
        var result = ""
        for c in resultArr {
            result.append(c)
        }
        return result
    }
}

Solution().findReplaceString("abcd", [0,2], ["ab","ec"], ["___","[]"])
