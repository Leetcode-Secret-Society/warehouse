class Solution:
    def decodeString(self, s: str) -> str:
        #3[a]2[bc]d
        #3[a2[b3[c]]]xyz
        stack = []
        current_digit = ""
        digits = []
        for i in range(len(s)):
            c = s[i]
            if c == "[":
                digits.append(int(current_digit))
                current_digit = ""
                stack.append(c)
            elif c == "]":
                #get brace content
                content = ""
                while len(stack) > 0 and stack[-1] != "[":
                    content += stack.pop()
                stack.pop() # pop "["
                digit = digits.pop()
                stack.extend(digit * content[::-1]) #using extend but not append...
            elif c.isdigit():
                current_digit += c
            else:
                stack.append(c)
            
        return "".join(stack)
