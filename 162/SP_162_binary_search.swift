extension Array {
    // Safely lookup an index that might be out of bounds,
    // returning nil if it does not exist
    func get(index: Int) -> Element? {
        if 0 <= index && index < count {
            return self[index]
        } else {
            return nil
        }
    }
}

class Solution {
    func findPeakElement(_ arr: [Int]) -> Int {
        var isPeak = false
        var lowerBound = 0
        var higherBound = arr.count - 1
        while lowerBound < higherBound {
            let currentIndex = lowerBound + (higherBound - lowerBound)/2
            let value = arr[currentIndex]
            let rightValue = arr.get(index: currentIndex + 1) ?? Int.min
//            print("\(currentIndex):\(value) | \(rightValue)")
            if value < rightValue {
                lowerBound = currentIndex + 1
            } else {
                higherBound = currentIndex
            }
        }
        return higherBound
    }
}
