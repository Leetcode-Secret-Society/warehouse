class Solution {
    var pointResults = [[Int]]()
    func dp(_ points: [Int],_ y: Int, width: Int) {
        //@see: https://leetcode.com/problems/maximum-number-of-points-with-cost/discuss/1344888/C++-dp-from-O(m-*-n-*-n)-to-O(m-*-n)/1014241
        if y==0 {
            pointResults.append(points)
            return
        }
        let dpPoints = pointResults[y-1]
        let zeroStartedWidth = width - 1
        var result = [Int](repeating: 0, count: width)
        var leftResults = [Int](repeating: 0, count: width)
        var rightResult = [Int](repeating: 0, count: width)
        leftResults[0] = dpPoints[0]
        rightResult[zeroStartedWidth] = dpPoints[zeroStartedWidth]
        for x in 1..<width {
            leftResults[x] = max(leftResults[x - 1] - 1, dpPoints[x])
            let reversedIndex = zeroStartedWidth - x
            rightResult[reversedIndex] = max(rightResult[reversedIndex + 1] - 1, dpPoints[reversedIndex])
        }
        
        
        for (x, currentPoint) in points.enumerated() {
            //            print("\(x)")
            //            print("\(currentPoint) + max(\(leftResults[x]) - \(x), \(rightResult[x]) + \(x))")
            result[x] = max(leftResults[x], rightResult[x]) + currentPoint
            //            print("=====================")
        }
        pointResults.append(result)
    }
    func maxPoints(_ points: [[Int]]) -> Int {
        let width = points[0].count
        for (y, pointsInY) in points.enumerated() {
            dp(pointsInY, y, width: width)
                       // print(pointResults)
                       // print("------------")
        }
        var finalResult = 0
        for result in pointResults.last ?? [] {
            finalResult = max(finalResult, result)
        }
        return finalResult
    }
}
