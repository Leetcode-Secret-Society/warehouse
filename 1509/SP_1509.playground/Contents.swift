class Solution {
    func minDifference(_ nums: [Int]) -> Int {
        if nums.count <= 4 { //most 3 moves
            return 0
        }
        //0,1,1,4,6,6,6
        let s = nums.sorted()
        let length = s.count - 1
        return min((s[length-0] - s[3]),
                   (s[length-1] - s[2]),
                   (s[length-2] - s[1]),
                   (s[length-3] - s[0]))
    }
}
Solution().minDifference([82,81,95,75,20])
//Solution().minDifference([6,6,0,1,1,4,6])
