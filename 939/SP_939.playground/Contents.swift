class Solution {
    func minAreaRect(_ points: [[Int]]) -> Int {
        var xMap = [Int:[Int]]()
        for point in points {
            let x = point.first!
            let y = point.last!
            if var points = xMap[x] {
                xMap[x]!.append(y)
            } else {
                xMap[x] = [y]
            }
        }
        for (x, ys) in xMap {
            xMap[x]?.sort()
        }
//        print(xMap)
        
        
        let sortedXs = xMap.keys.sorted()
        func findMinY(startYs: [Int], endYs: [Int]) -> Int? {
            
            var endYsIndexOffset = 0
            var yPair = [Int]()
            for startY in startYs {
                for endYsIndex in endYsIndexOffset..<endYs.count {
                    if startY == endYs[endYsIndex] {
                        endYsIndexOffset = endYsIndex
                        yPair.append(startY)
                    }
                }
            }
            var minY : Int?
//            print(yPair)
            for index in 0..<yPair.count {
                if index > 0 {
                    let yDiff = abs(yPair[index] - yPair[index-1])
                    minY = min(yDiff, minY ?? Int.max)
                }
            }
            
            return minY
        }
        
        var area : Int?

        for index in 0..<sortedXs.count {
            if index > 0 {
                let endX = sortedXs[index]
                for innerIndex in 0..<index {
                    let startX = sortedXs[innerIndex]
                    let diffX = endX - startX
                    if let minY = findMinY(startYs: xMap[startX]!,endYs: xMap[endX]!) {
                        let tempArea = minY * diffX
                        area = min(tempArea, area ?? Int.max)
//                        print("\(minY) \t* \(diffX)\t(\(endX) to \(startX))\t = \(tempArea) \t--> \(area)")
                    }
                }
                
            }
        }
        return area ?? 0
    }
}

14016300
Solution().minAreaRect([[39973,30270],[13301,37647],[13854,37647],[13301,1045],[13854,1045],[11401,37647],[13854,10339],[11401,1045],[11401,10339],[13301,30270],[39973,37647],[11401,30270],[39973,1045],[39973,10339]])


