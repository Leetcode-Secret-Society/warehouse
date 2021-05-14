
class Solution {
    func debugPrint(_ s:String) {
        if false {
            print(s)
        }
    }
    var stack = [Int:Int]()
    init(_ w: [Int]) {
        for (i,weight) in w.enumerated() {
            stack[i] = weight
        }
    }
    
    var pickStack = [Int:Int]()
    func pickIndex() -> Int {
        if pickStack.count == 0 {
            debugPrint("refill!")
            pickStack = stack
        }
        let random = Int.random(in: 0...pickStack.count-1)
        let randomedKey = Array(pickStack.keys)[random]
        guard
            var value = pickStack[randomedKey]
        else {
            return stack.count - 1
        }
        
        debugPrint("current stack:\(pickStack)")
//        print("============")
//        print(randomedKey)
//        print(value)
//        print("============")
        value -= 1
        let refillIfOneEmpty = true
        if refillIfOneEmpty {
            if value <= 0 {
                debugPrint("one ele is empty, refill!")
                pickStack.merge(stack) { (i, j) -> Int in
                    return i + j
                }
                pickStack[randomedKey]! -= 1
                debugPrint("\(stack)")
            }
        } else {
            if value <= 0 {
                debugPrint("remove:\(randomedKey)")
                pickStack.removeValue(forKey: randomedKey)
            } else {
                pickStack[randomedKey] = value
            }
        }
        
        return randomedKey
    }
}

let s = Solution.init([1,3])
for _ in 0...4 {
    print("======PICK:\(s.pickIndex())")
}
