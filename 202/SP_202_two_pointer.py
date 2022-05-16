class Solution:
    def isHappy(self, n: int) -> bool:
        #Two pointer
        dp = {}
        def get_happy(num :int):
            if dp.get(num) != None:
                return dp[num]
            n_list = list(map(int,str(num)))
            result = 0
            for digit in n_list:
                result += int(math.pow(digit, 2))
            dp[num] = result
            return result
                
        slow = n
        fast = get_happy(n) #to get loop
        while fast != 1 and slow != fast:
            slow = get_happy(slow)
            fast = get_happy(get_happy(fast))
        return fast == 1
    
    def isHappyPureDP(self, n: int) -> bool:
        dp = {}
            
        num = n
        while num != 1:
            if dp.get(num) != None: #if making a repeat value, means a loop, dead end
                return False
            n_list = list(map(int,str(num)))
            result = 0
            for digit in n_list:
                result += int(math.pow(digit, 2))
            dp[num] = result
            num = result
        return True
