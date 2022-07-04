class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def doBackspace(s: str) -> List:
            s_stack = []    
            for char in s:
                if char != '#':
                    s_stack.append(char)
                else:
                    if len(s_stack) > 0:
                        s_stack.pop(-1)
            return s_stack
        if doBackspace(s) == doBackspace(t):
            return True
        return False
