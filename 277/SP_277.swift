/**
 * The knows API is defined in the parent class Relation.
 *     func knows(_ a: Int, _ b: Int) -> Bool;
 */

class Solution : Relation {
    
    func findCelebrity(_ n: Int) -> Int {
        var potentialCelebrities = Set(0..<n)
        func isCelebrity(_ people: Int) -> Bool{
            // print("[\(people)]")
            for target in 0..<n {
                if people == target {
                    //not asking self
                } else {
                    // print(target)
                    if knows(people, target) == false { //A-->B (X), B won't be celebrity, A might be
                        potentialCelebrities.remove(target)
                        if knows(target, people) == false { //B-->A(X), A won't be celebrity, end
                            potentialCelebrities.remove(people)
                            return false
                        } else {
                        }
                    } else { //A-->B (O), means A won't be celebrity,
                        potentialCelebrities.remove(people)
                        return false
                    } 
                }
            }
            return true
        }
        for people in 0..<n {
            // print(potentialCelebrities)
            if potentialCelebrities.contains(people) {
                if isCelebrity(people) {
                   return people
                }
            }
        }
        return -1
    }
}
