class Solution {
    func customSortString(_ order: String, _ s: String) -> String {
        var oArr = Array(order)
        var toAppend = [Character:Int]()
        var toKeep = [Character]()
        for (i, c) in s.enumerated() {
            if let index = oArr.firstIndex(of: c)  {
                toAppend[c] = (toAppend[c] ?? 0) + 1
            }
            else {
                toKeep.append(c)
            }
        }
        // print(toAppend)
        var toAppendArr = [Character]()
        for i in 0..<oArr.count {
            let count = toAppend[oArr[i]] ?? 0
            for j in 0..<count {
                toAppendArr.append(oArr[i])
            }
        }
        return String(toKeep+toAppendArr)
    }
}
