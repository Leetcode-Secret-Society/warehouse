class Solution {
    func maxAreaOfIsland(_ grid: [[Int]]) -> Int {
        var color = [Int:[String:Int]]()
        var newColorCount = 0
        func setColor(y: Int, x : Int) {
            let pos = "\(x),\(y)"
            var isNewColor = true
            var topGotColor:Int? = nil
            var leftGotColor:Int? = nil
            for i in color.keys {
                let aColor = color[i]!
                if aColor["\(x-1),\(y)"] != nil {
                    leftGotColor = i
                    isNewColor = false
                }
                else if aColor["\(x),\(y-1)"] != nil {
                    topGotColor = i
                    isNewColor = false
                }
            }
//            print("\(x),\(y)-new:\(isNewColor) top:\(topGotColor) left:\(leftGotColor)")
            
            if isNewColor {
                newColorCount += 1
                color[newColorCount] = [pos:newColorCount]
            }
            else if let topColor = topGotColor, let leftColor = leftGotColor {
                if topColor != leftColor, var aColor = color[topColor], var bColor = color[leftColor]{
                    aColor.merge([pos : newColorCount]) { (a, b) -> Int in
                        a
                    }
                    aColor.merge(bColor) { (a, b) -> Int in
                        a
                    }
                    color[topColor] = aColor
                    color[leftColor] = nil
                } else {
                    color[topColor]?.merge([pos : newColorCount]) { (a, b) -> Int in
                        a
                    }
                }
            } else if let topColor = topGotColor {
                color[topColor]?.merge([pos : newColorCount]) { (a, b) -> Int in
                    a
                }
            } else if let leftColor = leftGotColor {
                color[leftColor]?.merge([pos : newColorCount]) { (a, b) -> Int in
                    a
                }
            }
            
        }
        for y in 0...grid.count - 1 {
            for x in 0...grid[y].count - 1 {
                if grid[y][x] == 1 {
                    setColor(y: y, x: x)
                }
            }
        }
//        print(color)
        var count = 0
        for aColor in color.values {
            count = max(aColor.count,count)
        }
        return count
    }
}
