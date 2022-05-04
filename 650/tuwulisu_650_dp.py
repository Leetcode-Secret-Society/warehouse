class Solution:
    def findFirstPrime(self, n):
        for i in range(2, math.ceil(math.sqrt(n))+1):
            if n%i==0:
                return i
        return n
    def minSteps(self, n: int) -> int:
        if n==1:
            return 0
        elif n==2:
            return 2
        elif n==3:
            return 3
        firstPrime = self.findFirstPrime(n)
        if firstPrime == n:
            return n
        else:
            return self.minSteps(int(n/firstPrime))+firstPrime

