class Solution {
    init() {
    }
    var grid :[[Int]]?
    func dPrint(_ s:String) {
        if true {
            return
        }
        print(s)
    }
    func dfs(x:Int, y:Int, x_bounds: Int, y_bounds: Int) -> Bool{
        dPrint("dfs[\(x)-\(y)]")
        if x < 0 || x >= x_bounds || y < 0 || y >= y_bounds {
            dPrint("false")
            return false
        }
        
        if grid?[x][y] == 1 || grid?[x][y] == 2 || grid?[x][y] == 9{
            dPrint("true")
            return true
        }
        dPrint("     go deep")
        grid?[x][y] = 2 //visited
        var isClosed = true
        // from: https://leetcode.com/problems/number-of-closed-islands/discuss/425135/Java-Very-Simple-DFS-Solution/383149
        // if isClosed = isClosed && dfs(grid,m,n), your island will be partially filled,
        // and even worse, the another part may form a 'island' which is wrong.
        // ----
        // if isClose runs first, it wont run dfs if isClosed == false, we need running to end to
        // get bounds to affect other area.
        // using last test case below, and testing with `dfs() && isClosed` / `isClosed && dfs()`
        // you will find `dfs() && isClosed` runs 13 times, `isClosed && dfs()` only runs 8 times
        dPrint("     right")
        isClosed = dfs(x: x+1, y: y, x_bounds: x_bounds, y_bounds: y_bounds) && isClosed
        dPrint("     left")
        isClosed = dfs(x: x-1, y: y, x_bounds: x_bounds, y_bounds: y_bounds) && isClosed
        dPrint("     down")
        isClosed = dfs(x: x, y: y+1, x_bounds: x_bounds, y_bounds: y_bounds) && isClosed
        dPrint("     top")
        isClosed = dfs(x: x, y: y-1, x_bounds: x_bounds, y_bounds: y_bounds) && isClosed
        
//        isClosed = isClosed && dfs(x: x+1, y: y, x_bounds: x_bounds, y_bounds: y_bounds)
//        isClosed = isClosed && dfs(x: x-1, y: y, x_bounds: x_bounds, y_bounds: y_bounds)
//        isClosed = isClosed && dfs(x: x, y: y+1, x_bounds: x_bounds, y_bounds: y_bounds)
//        isClosed = isClosed && dfs(x: x, y: y-1, x_bounds: x_bounds, y_bounds: y_bounds)
        dPrint("\(x)-\(y) = \(isClosed)")
        
        return isClosed
    }
    func closedIsland(_ grid: [[Int]]) -> Int {
        self.grid = grid
        var result = 0
        let x_bounds = grid.count
        let y_bounds = grid[0].count
        for i in 0..<x_bounds {
            for j in 0..<y_bounds {
                if self.grid?[i][j] == 0 {
                    if dfs(x: i, y: j, x_bounds: x_bounds, y_bounds: y_bounds) {
//                        dPrint("result: \(i)-\(j)")
                        self.grid?[i][j] = 9 //9 means counts as an isolated island, for debugging usage
                        result+=1
                    }
                }
            }
        }
        for line in 0..<grid.count {
            dPrint("\(self.grid?[line])")
        }
        return result
    }
}
//Solution().closedIsland(
//    [[1,1,1,1,1,1,1,0],
//     [1,0,0,0,0,1,1,0],
//     [1,0,1,0,1,1,1,0],
//     [1,0,0,0,0,1,0,1],
//     [1,1,1,1,1,1,1,0]])
//Solution().closedIsland(
//    [[0,0,1,1,0,1,0,0,1,0],
//     [1,1,0,1,1,0,1,1,1,0],
//     [1,0,1,1,1,0,0,1,1,0],
//     [0,1,1,0,0,0,0,1,0,1],
//     [0,0,0,0,0,0,1,1,1,0],
//     [0,1,0,1,0,1,0,1,1,1],
//     [1,0,1,0,1,1,0,0,0,1],
//     [1,1,1,1,1,1,0,0,0,0],
//     [1,1,1,0,0,1,0,1,0,1],
//     [1,1,1,0,1,1,0,1,1,0]])

//TEST CASE
Solution().closedIsland(
    [[1,1,1,1],
     [1,0,0,1],
     [1,0,1,1]]
)
