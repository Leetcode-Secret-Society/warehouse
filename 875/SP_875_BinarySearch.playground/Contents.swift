import Foundation

class Solution {
    func getHoursCost(_ k : Int, _ piles: [Int]) -> Int {
        if k==0 {
            return Int.max
        }
        var hoursCost = 0
        for pile in piles {
            hoursCost += Int(ceil(Double(pile)/Double(k)))
        }
        return hoursCost
    }
    func getBounds(_ piles: [Int], _ hoursAvaible: Int) -> (lowerBound: Int, upperBound: Int) {
        var total = 0
        var maxPile = 0
        for pile in piles {
            maxPile = max(pile, maxPile)
            total += pile
        }
        total /= hoursAvaible
        return (total, maxPile)
        
//        let sortedPiles = piles.sorted()
//        var lowerBound = sortedPiles.first!/hoursAvaible
//        var upperBound = sortedPiles.last!
//        return (lowerBound, upperBound)
        
//        return (0, 1_000_000_000)
    }
    func binarySearch(_ piles: [Int], _ hoursAvaible: Int) -> Int {
        var bounds = getBounds(piles, hoursAvaible)
        var lowerBound = bounds.lowerBound
        var upperBound = bounds.upperBound
        while lowerBound < upperBound {
            let mid = lowerBound + (upperBound - lowerBound) / 2
            let hCost = getHoursCost(mid, piles)
//            print("mid:\(mid)\t-\thCost:\(hCost)")
            if hCost <= hoursAvaible {
                upperBound = mid
            } else {
                lowerBound = mid + 1
            }
        }
        return lowerBound
    }
    func bruteForce(_ sortedPiles: [Int], h: Int) -> Int {
        func pass(_ k : Int, _ piles: [Int], _ h: Int) -> Bool {
            if k==0 {
                return false
            }
            return getHoursCost(k, piles) <= h
        }
        let max = sortedPiles.last!
        let min = sortedPiles.first!
        for i in Int(min/h)...max {
            if (pass(i,sortedPiles,h)) {
                return i
            }
        }
        return max
    }
    func minEatingSpeed(_ piles: [Int], _ h: Int) -> Int {
        return binarySearch(piles, h)
    }
}

Solution().minEatingSpeed([30,11,23,4,20], 8)
//Solution().pass(10, [30,11,23,4,20].sorted(), 8)
