class Solution {
    func minSteps(_ s: String, _ t: String) -> Int {
        let sArr = Array(s)
        let tArr = Array(t)
//        var sDic = [Character:Int]()
//        var tDic = [Character:Int]()
        var dic = [Character:Int]()
        sArr.forEach { c in
            dic[c] = (dic[c] ?? 0) + 1
        }
        tArr.forEach{ c in
            dic[c] = (dic[c] ?? 0) - 1
        }
        let aToZ = Array("abcdefghijklmnopqrstuvwxyz")
        var count = 0
        for key in aToZ {
//            let sVal = sDic[key] ?? 0
//            let tVal = tDic[key] ?? 0
//            count += abs(sVal - tVal)
            count += abs(dic[key] ?? 0)
        }
        return count
    }
}

Solution().minSteps("eeee","ffff")
Solution().minSteps("leetcode","coats")
