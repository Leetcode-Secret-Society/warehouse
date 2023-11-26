class Solution {
    func orangesRotting(_ grid: [[Int]]) -> Int {
        var stack = [[Int]]()
        var count = 0
        var nextStack = [[Int]]()
        var visited = Set<[Int]>()
        var depth = 0
        for i in 0..<grid.count {
            for j in 0..<grid[0].count {
                if grid[i][j] == 2 {
                    visited.insert([i,j])
                    stack.append([i,j])
                    count += 1
                }
                else if grid[i][j] == 1 {
                    count += 1
                }
            }
        }
        let directions = [[1,0],[0,1],[-1,0],[0,-1]]
        while let popped = stack.popLast() {
            for direction in directions {
                let toRotten = [popped[0]+direction[0], popped[1]+direction[1]]
                if toRotten[0] >= 0 && toRotten[0] < grid.count && toRotten[1] >= 0 && toRotten[1] < grid[toRotten[0]].count {
                    if grid[toRotten[0]][toRotten[1]] == 1 && visited.contains(toRotten) == false {
                        visited.insert(toRotten)
                        nextStack.append(toRotten)
                    }
                }
            }
            // print((depth ,popped ,stack, nextStack))
            if stack.count == 0 && nextStack.count > 0{
                depth += 1
                stack.append(contentsOf: nextStack)
                nextStack.removeAll()
            }
        }
        // print(count)
        // print(visited)
        // return depth
        return count == visited.count ? depth : -1
    }
}
