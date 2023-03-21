class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        step = 0
        while target>startValue:
            if target%2==0:
                target//=2
            else:
                target+=1
            step+=1
        return step+startValue-target
