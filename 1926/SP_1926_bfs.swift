class Solution {
    let directions = [(1,0),(0,1),(-1,0),(0,-1)]
    var stack = [(Int,Int)]()
    var nextStack = [(Int,Int)]()
    var depth = 0
    var visited = Set<[Int]>()
    
    func nearestExit(_ maze: [[Character]], _ entrance: [Int]) -> Int {
        stack.append((entrance[0],entrance[1]))
        while let posistion = stack.popLast() {
            let posistionInArray = [posistion.0,posistion.1]
            if visited.contains(posistionInArray) == false {
                // print((posistion,maze.count, maze[posistion.0].count))
                visited.insert(posistionInArray)
                for direction in directions {
                    let target = (direction.0 + posistion.0, direction.1 + posistion.1)
                    if target.0 < maze.count && target.0 >= 0 && target.1 < maze[posistion.0].count && target.1 >= 0 {
                        if maze[target.0][target.1] == "." {
                            nextStack.append(target)
                            // print("pass-\(target)")
                        }
                        else {
                            // print("wall-\(target)")
                        }
                    }
                    else if posistion.0 != entrance[0] || posistion.1 != entrance[1] {
                    // else {
                        //answer
                        // print("exit-\(posistion)-\(target)")
                        return depth
                    }
                }
            }
            if stack.count == 0 {
                // print("add depth-\(nextStack)")
                depth += 1
                stack.append(contentsOf: nextStack)
                nextStack.removeAll()
            }
        }

        return -1
    }
}

/*
[["+",".","+","+","+","+","+"],
["+",".","+",".",".",".","+"],
["+",".","+",".","+",".","+"],
["+",".",".",".","+",".","+"],
["+","+","+","+","+",".","+"]]
*/
