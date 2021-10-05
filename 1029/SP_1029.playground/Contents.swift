
class Solution {
    func twoCitySchedCost(_ costs: [[Int]]) -> Int {
        let n = Int(costs.count/2)
        var diffs = [Int:Int]()//diff:cost-index
        for (i, cost) in costs.enumerated() {
            let diff = cost[0] - cost[1]
            diffs[i] = diff
        }
        
        let sorted = diffs.sorted { (a, b) -> Bool in
            a.value < b.value
        }
        
        var result = 0
        for i in 0..<n {
            result += costs[sorted[i].key].first ?? 0
            result += costs[sorted[i+n].key].last ?? 0
        }
        return result
    }
}
Solution().twoCitySchedCost([[10,10],[20,20],[40,100],[40,200]])
Solution().twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]])
Solution().twoCitySchedCost([[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]])
Solution().twoCitySchedCost([[10,10],[30,30],[400,400],[30,30]])
/*
[[10,10],[20,20],[40,100],[40,200]]
    0       0       -60    -160
[10,10,0]
    [10,10,0],[20,20,0]---
        [40,100,-60],[10,10,0]---[20,20,0]
            [40,200,-160],[40,100,-60]---[20,20,0],[10,10,0]
        
 [[10,20],[30,200],[400,50],[30,20]]
    -10      -170      350     10
 [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
    -500      400       300        50       700        100
 */
