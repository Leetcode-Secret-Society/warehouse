class Solution {
    var pointResults = [[Int]]()
    func dp(_ points: [Int],_ y: Int) {
        if y==0 {
            pointResults.append(points)
            return
        }
        var dpPoints = pointResults[y-1]
        var result = [Int](repeating: 0, count: points.count)
        for (x, currentPoint) in points.enumerated() {
            for (dp_x, dpPoint) in dpPoints.enumerated() {
                print("\(x) to \(dp_x)")
                print("\(currentPoint) - \(abs(x-dp_x)) + \(dpPoint), \(result[x])")
                result[x] = max(currentPoint - abs(x-dp_x) + dpPoint, result[x])
            }
        }
        pointResults.append(result)
    }
    func maxPoints(_ points: [[Int]]) -> Int {
        
        for (y, pointsInY) in points.enumerated() {
            print("------------")
            dp(pointsInY, y)
            print(pointResults)
            print("------------")
        }
        var finalResult = 0
        for result in pointResults.last ?? [] {
            finalResult = max(finalResult, result)
        }
        return finalResult
    }
}

Solution().maxPoints([[1,5],[2,3],[4,2]])
