class Solution {
    func multiply(_ multiplier: Int, multiSource:String) -> String {
        return String.init(repeating: multiSource,count: multiplier)
    }
    func getDigitsBeforeBracket(_ input:String, bracketStartIndex: String.Index) -> (digitCount:Int,digits:Int){
        var target = 0
        var start = bracketStartIndex
        var digitCounter = 0
        //        let a = input[input.index(before: start)..<start]
        
        while var digit = Int(input[input.index(before: start)..<start]) {
//            print("digit:\(digit)-\(input.distance(from: input.startIndex, to: start))")
            for _ in 0..<digitCounter {
//                print("a")
                digit = digit * 10
            }
            target += digit
            digitCounter += 1
            if input.distance(from: input.startIndex, to: start) == 1 {
                break
            } else {
                start = input.index(before: start)
            }
        }
        return (digitCounter,target)
    }
    func findBracketPair(_ input: String) -> String? {
        var target = input
        guard let start = input.lastIndex(of: "["),
              let end = input[start..<input.endIndex].firstIndex(of: "]") else {
            return nil
        }
        let bracketString = input[input.index(after:start)..<end]
        let tuple = getDigitsBeforeBracket(input, bracketStartIndex: start)
        let multiplier = tuple.digits
        
        let multiplied = multiply(Int(multiplier) , multiSource: String(bracketString))
        
        target.replaceSubrange(input.index(start, offsetBy: -1*tuple.digitCount)...end, with: multiplied)
        return target
    }
    func decodeString(_ s: String) -> String {
        var target = s
        while let handled = findBracketPair(target) {
            target = handled
        }
        return target
    }
}
