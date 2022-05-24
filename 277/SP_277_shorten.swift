/**
 * The knows API is defined in the parent class Relation.
 *     func knows(_ a: Int, _ b: Int) -> Bool;
 */

class Solution : Relation {
    
    func findCelebrity(_ n: Int) -> Int {
        var potentialCelebrity = 0
        var cache = [String: Bool]()
        func cacheKnows(_ a:Int, _ b:Int) -> Bool {
            let key = "\(a),\(b)"
            if cache[key] == nil {
                cache[key] = knows(a,b)
            }
            return cache[key]!
        }
        func isCelebrity(_ people: Int) -> Bool{
            for target in 0..<n {
                if people == target {
                    //not asking self
                } else {
                    if !cacheKnows(target, people) || cacheKnows(people, target) {
                        return false
                    }
                }
            }
            return true
        }
        for people in 0..<n {
            if cacheKnows(potentialCelebrity, people) {
                potentialCelebrity = people
            }
        }
        if isCelebrity(potentialCelebrity) {
            return potentialCelebrity
        }
        return -1
    }
}
