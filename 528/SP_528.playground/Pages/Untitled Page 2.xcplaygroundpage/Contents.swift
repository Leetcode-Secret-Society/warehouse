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
        totalWeight = 0
        for i in w {
            totalWeight += i
            expanded.append(totalWeight)
        }
        //[1,4]
        print(expanded)
    }
    var fakeRandom = -1
    let fakeTest = true
    func pickIndex() -> Int {
        var random = 0
        if fakeTest  {
            fakeRandom += 1
            random = fakeRandom%totalWeight
        } else {
            random = Int.random(in: 0...totalWeight-1) //0~3
        }

        
//        print("random:\(random)")
        //[0-1--4], 0~1->#0, 1~4->#1
        
        //linear
        for (i, w) in expanded.enumerated() { //1,4
            //1 < 2
            //4 > 2
            if w > random {
                return i
            }
        }
        
        //binary
        let index = expanded.binarySearch { (i) -> Bool in
            return i <= random
        }
        return index
    }
}

let s = Solution.init([1,3])
for _ in 0...4 {
    print(s.pickIndex())
}
