class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #using stack
        stack = []
        operators = ["+","-","*","/"]
        for index, input in enumerate(tokens):
            stack.append(input)
            if input in operators:
                stack.pop()
                num2 = int(stack[-1])
                stack.pop()
                num1 = int(stack[-1])
                stack.pop()
                if input == "+":
                    stack.append(str(num1+num2))
                elif input == "-":
                    stack.append(str(num1-num2))
                elif input == "*":
                    stack.append(str(num1*num2))
                elif input == "/":   
                    stack.append(str(int(num1/num2)))
        
        # ((10 * (6 / ((9 + 3) * -11)))
        # print(stack)
        return int(stack[0])
