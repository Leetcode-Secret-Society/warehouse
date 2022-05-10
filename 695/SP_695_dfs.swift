extension Array {
    func getSafely(_ index: Int) -> Element? {
        if index < 0 {
            return nil
        }
        if index >= self.count {
            return nil
        }
        return self[index]
    }
}
class Solution {
    func debugPrint(_ s: String) {
        if false {
            print(s)
        }
    }
    func maxAreaOfIsland(_ grid: [[Int]]) -> Int {
        var dpGridVal = [String:Int]()
        var visited = [String:Bool]()
        
        func dp(y:Int, x:Int)-> Int {
            if let val = dpGridVal["\(y)-\(x)"] {
                //                debugPrint("dped!")
                return val
            }
            debugPrint("visit:\(y),\(x)")
            visited["\(y)-\(x)"] = true
            var value = 0
            func visitedOrEmpty(y:Int, x:Int) -> Bool {
                grid.getSafely(y)?.getSafely(x) ?? 0 == 0 || visited["\(y)-\(x)"] == true
            }
            if grid.getSafely(y)?.getSafely(x) ?? 0 == 0 {
                value = 0
            }
            else if
                 visitedOrEmpty(y: y+1, x: x) &&
                    visitedOrEmpty(y: y, x: x+1) &&
                    visitedOrEmpty(y: y, x: x-1) &&
                    visitedOrEmpty(y: y-1, x: x)
            {
                debugPrint("base!\(y),\(x)")
                value = 1
            } else {
                debugPrint("dp!")
                value += 1
                if visited["\(y+1)-\(x)"] != true {
                    value += dp(y: y+1, x: x)
                }
                if visited["\(y)-\(x+1)"] != true {
                    value += dp(y: y, x: x+1)
                }
                if visited["\(y-1)-\(x)"] != true {
                    value += dp(y: y-1, x: x)
                }
                if visited["\(y)-\(x-1)"] != true {
                    value += dp(y: y, x: x-1)
                }
            }
            dpGridVal["\(y)-\(x)"] = value
            return value
        }
        
        var biggest = 0
        for y in 0...grid.count - 1 {
            for x in 0...grid[y].count - 1 {
                biggest = max(dp(y: y, x: x),biggest)
            }
        }
//        print("A:\(dpGridVal)")
        return biggest
    }
}
