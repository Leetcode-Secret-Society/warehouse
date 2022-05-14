class Solution {
    
    func decodeString(_ s: String) -> String {
        var stack = [Character]()
        for charc in s {
            if charc == Character("]") {
                //do multiply
                var popped = Character(" ")
                var multiplier = ""
                while (popped != "[") {
                    popped = stack.removeLast()
                    multiplier.append(popped)
                    // print(popped)
                }
                
                multiplier = String(multiplier.dropLast().reversed())
                
                var times = ""
                while (stack.last?.isNumber == true) {
                    popped = stack.removeLast()
                    times.append(popped)
                }
                times = String(times.reversed())
                //"4[2[ab]]1[c]"
                // print(multiplier)
                // print(times)
                let multiplierArray = Array(multiplier)
                for i in 0..<(Int(times) ?? 1) {
                    stack+=multiplierArray
                }
            }
            else {
                stack.append(charc)
            }
        }
        // print(stack)
        return String(stack)
    }
}
