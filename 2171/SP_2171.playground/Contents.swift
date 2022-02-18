class Solution {
    func minimumRemoval(_ beans: [Int]) -> Int {
        var sortedBeans = beans.sorted()
        var result = Int.max
        var prev_result = Int.max
        var prev_target = 0
        var target = 0
        for i in 0..<beans.count {
            target = sortedBeans[i]
//            if target == prev_target {
//                continue
//            }
            var tmp = 0
            if prev_result == Int.max {
                for fromBegin in 0..<i {
                    tmp += sortedBeans[fromBegin]
                }
                for toEnd in i..<beans.count {
                    tmp += sortedBeans[toEnd] - target
                }
            } else {
                
                let diff = target - prev_target
                tmp = prev_result + prev_target - diff * (beans.count - i)
//                print("\(i)-diff:\(diff)-target:\(target)-prev:\(prev_target)")
                
            }
            prev_result = tmp
            result = min(tmp, result)
            prev_target = target
        }
        return result
    }
}
Solution().minimumRemoval([4,1,6,5]) //4
Solution().minimumRemoval([2,10,3,2]) //7

// 2,2,3,10
//-----------
// 2,2,2,2 = 9
// 0,2,2,2 = 11 = lastResult + prev - diff*i..end
// 0,0,3,3 =
// 0,0,0,10 =
