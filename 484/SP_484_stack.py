class Solution:
    def findPermutation(self, s: str) -> List[int]:
        n = len(s) + 1
        
        result = list()
        d_stack = list()
        for i in range(1, n):
            curr_c = s[i - 1]
            if curr_c == "I":
                result.append(i)
                while len(d_stack) > 0:
                    result.append(d_stack.pop())
            else:
                d_stack.append(i)
        
        #last word handling
        if s[-1] == "D":
            result.append(n)
            while len(d_stack) > 0:
                        result.append(d_stack.pop())       
        if s[-1] == "I":
            result.append(n)
        return result
