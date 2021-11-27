class Solution {
    func asteroidCollision(_ asteroids: [Int]) -> [Int] {
        var result = [Int]()
        for asteroid in asteroids {
            var isAsteroidDestroied = false
            while let leftAsteroid = result.popLast() {
                let shouldCollide = leftAsteroid > 0 && asteroid < 0
                if shouldCollide {
                    let absLeft = abs(leftAsteroid)
                    let absAstro = abs(asteroid)
                    if absLeft == absAstro {
                        isAsteroidDestroied = true
                        break
                    }
                    else if absLeft > absAstro {
                        isAsteroidDestroied = true
                        result.append(leftAsteroid)
                        break
                    }
                } else {
                    result.append(leftAsteroid)
                    break
                }
            }
            if isAsteroidDestroied == false {
                result.append(asteroid)
            }
        }
        return result
    }
}
Solution().asteroidCollision([10,2,-2,-5,11])
//Solution().asteroidCollision([-2,-1,1,2])
Solution().asteroidCollision([2,-1,-2])
//Solution().asteroidCollision([-2,-2,1,-2])
