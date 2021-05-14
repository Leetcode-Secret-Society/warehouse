extension Array {
    
    func objectAt(_ index:Int) -> Any? {
        if index < 0 {
            return nil
        }
        if index >= self.count {
            return nil
        }
        return self[index]
    }
}
extension RandomAccessCollection {
    /// Finds such index N that predicate is true for all elements up to
    /// but not including the index N, and is false for all elements
    /// starting with index N.
    /// Behavior is undefined if there is no such N.
    func binarySearch(predicate: (Element) -> Bool) -> Index {
        var low = startIndex
        var high = endIndex
        while low != high {
            let mid = index(low, offsetBy: distance(from: low, to: high)/2)
            if predicate(self[mid]) {
                low = index(after: mid)
            } else {
                high = mid
            }
        }
        return low
    }
}
class Solution {
    var expanded = [Int]()
    var totalWeight = 0
    init(_ w: [Int]) {
//        for (i,weight) in w.enumerated() {
//            expanded.append( contentsOf: Array.init(repeating: i, count: weight))
//        }
//        expanded.shuffle()
        totalWeight = 0
        for i in w {
            totalWeight += i
            expanded.append(totalWeight)
        }
        print(expanded)
    }
    var fakeRandom = -1
    func pickIndex() -> Int {
        let random = Int.random(in: 0...totalWeight-1)
//        fakeRandom += 1
//        let random = fakeRandom
        
//        print("random:\(random)")
        
        //[0-1---4], 0~1->1, 1~4->1
        
        //linear
//        for (i, w) in expanded.enumerated() {
//            if w > random {
//                return i
//            }
//        }
        
        //binary
        let index = expanded.binarySearch { (i) -> Bool in
            return i <= random
        }
        return index
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * let obj = Solution(w)
 * let ret_1: Int = obj.pickIndex()
 */

let s = Solution([2,4])
for _ in 0...4 {
    print(s.pickIndex())
}
