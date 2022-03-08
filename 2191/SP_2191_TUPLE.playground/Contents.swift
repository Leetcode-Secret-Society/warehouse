extension StringProtocol  {
    var digits: [Int] { compactMap(\.wholeNumberValue) }
}
class Solution {
    func sortJumbled(_ mapping: [Int], _ nums: [Int]) -> [Int] {
        var mappedNums = [(Int,Int)]()
        for num in nums {
            let digits = String(num).digits
            var mapped = ""
            for digit in digits {
                mapped.append("\(mapping[digit])")
            }
            mappedNums.append((num,Int(mapped)!))
        }
        mappedNums.sort { (a, b) -> Bool in
            a.1 < b.1
        }
        print(mappedNums)
        return mappedNums.map{$0.0}
    }
}
Solution().sortJumbled([8,9,4,0,2,1,3,5,7,6], [991,338,38])
