extension StringProtocol  {
    var digits: [Int] { compactMap(\.wholeNumberValue) }
}
class Solution {
    func sortJumbled(_ mapping: [Int], _ nums: [Int]) -> [Int] {
        var mappedNums = [Int:[Int]]()
        for num in nums {
            let digits = String(num).digits
            var mapped = ""
            for digit in digits {
                mapped.append("\(mapping[digit])")
            }
            var mNums = mappedNums[Int(mapped)!] ?? [Int]()
            mNums.append(num)
            mappedNums[Int(mapped)!] = mNums
        }
        var result = [Int]()
//        print(mappedNums)
        
        for key in mappedNums.keys.sorted() {
            let mNums = mappedNums[key]!
            for num in mNums {
                result.append(num)
            }
        }
        return result
    }
}
