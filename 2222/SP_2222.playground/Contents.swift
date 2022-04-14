class Solution {
    func numberOfWays(_ s: String) -> Int {
        var zeroSum = 0
        var oneSum = 0
        let zeroChara = Character("0")
        for c in s {
            if c == zeroChara {
                zeroSum += 1
            }
        }
        oneSum = s.count - zeroSum
        
        var currentZeroSum = 0
        var currentOneSum = 0
        var result = 0
        for c in s {
            if c == zeroChara {
                currentZeroSum += 1
                result += currentOneSum * (oneSum - currentOneSum)
            }
            else {
                currentOneSum += 1
                result += currentZeroSum * (zeroSum - currentZeroSum)
            }
        }
        
        return result
    }
}
Solution().numberOfWays("100111000011111")

/*
target
101
010

in:00 11 0 1
2,2,1,1
 
 odd * even * odd + even * odd * even

2,2,1 + 2,1,1
in: 111 00
3,2

in 1 00 111 0000 11111
1,2,3,4,5
        (1*2+(1+3)*4)
1*2*3 + (1*2*5 + 1*4*5 + 3*4*5) + 2*3*4
oddSum * currentEven or evenSum * currentOdd

1,2,3,4,5,6,7,8

 1*2*3 + (1*2+1*4+3*4)*5
*/
