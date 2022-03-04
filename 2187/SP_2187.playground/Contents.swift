import Darwin
class Solution {
    func minimumTime(_ time: [Int], _ totalTrips: Int) -> Int {
        var tripTime = 0
        var tripCount = 0
        var worst = time.min()! * totalTrips
        var best = worst/time.count
        tripTime = Int((best+worst)/2)
        if time.count == 1 {
            return time.first! * totalTrips
        }
        while worst > best{
            tripCount = 0
            tripTime = Int(best + (worst-best)/2)
            for bus in time {
                tripCount += tripTime/bus
            }
            //            print("b:\(best)-t:\(tripTime)-w:\(worst)- TC:\(tripCount)")
            if tripCount >= totalTrips {
                worst = tripTime
            } else {
                best = tripTime + 1
            }
        }
        return best
    }
}
Solution().minimumTime([1,2,3], 5)
//Solution().minimumTime([5,10,10],9)
//Solution().minimumTime([2,2], 5)
/*
9 times
1,1,1 -> times/count * min
1,100000000000,100000000000 -> 10
*/
