class Solution {
    func asteroidCollision(_ asteroids: [Int]) -> [Int] {
        var result = [Int]()
        for asteroid in asteroids {
            var isAsteroidDestroied = false
            var collidedLeftAstro = 0
            for leftAsteroid in result.reversed() {
                let shouldCollide = leftAsteroid > 0 && asteroid < 0
                if shouldCollide {
                    let absLeft = abs(leftAsteroid)
                    let absAstro = abs(asteroid)
                    if absLeft == absAstro {
                        isAsteroidDestroied = true
                        collidedLeftAstro += 1
                        break
                    }
                    else if absLeft > absAstro {
                        isAsteroidDestroied = true
                        break
                    }
                    else {
                        collidedLeftAstro += 1
                    }
                }
            }
            result.removeLast(collidedLeftAstro)
            if isAsteroidDestroied == false {
                result.append(asteroid)
            }
        }
        return result
    }
}
//Solution().asteroidCollision([10,2,-2,-5,11])
//Solution().asteroidCollision([-2,-1,1,2])
//Solution().asteroidCollision([2,-1,-2])
Solution().asteroidCollision([-2,-2,1,-2])
