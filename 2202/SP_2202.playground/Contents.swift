class Solution {
    func maximumTop(_ nums: [Int], _ k: Int) -> Int {
        //exception 1
        if k == 0 {
            return nums.first!
        }
        //exception 2, cannot finish if odd steps (empty array)
        if nums.count == 1 && k >= 1 {
            if k % 2 == 0 {
                return nums.first!
            }
            return -1
        }
        var result = Int.min
        //cannot pick k th
        for i in 0..<min(k-1, nums.count) {
            result = max(result , nums[i])
        }
        //pick the last one if all remove
        if k < nums.count {
            result = max(result, nums[k])
        }
        return result
    }
}

//Solution().maximumTop([35,43,23,86,23,45,84,2,18,83,79,28,54,81,12,94,14,0,0,29,94,12,13,1,48,85,22,95,24,5,73,10,96,97,72,41,52,1,91,3,20,22,41,98,70,20,52,48,91,84,16,30,27,35,69,33,67,18,4,53,86,78,26,83,13,96,29,15,34,80,16,49], 15)

//Solution().maximumTop([91,98,17,79,15,55,47,86,4,5,17,79,68,60,60,31,72,85,25,77,8,78,40,96,76,69,95,2,42,87,48,72,45,25,40,60,21,91,32,79,2,87,80,97,82,94,69,43,18,19,21,36,44,81,99], 2)


Solution().maximumTop([4,6,1,0,6,2,4],0)
