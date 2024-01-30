from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            "+": self.addition,
            "-": self.subtraction,
            "/": self.division,
            "*": self.multiplication,
        }
        stack = []
        for token in tokens:
            if token in operations:
                b = stack.pop()
                a = stack.pop()
                stack.append(operations[token](a, b))
            else:
                stack.append(int(token))
        return stack.pop()

    def addition(self, a: int, b: int) -> int:
        return a + b

    def subtraction(self, a: int, b: int) -> int:
        return a - b

    def multiplication(self, a: int, b: int) -> int:
        return a * b

    def division(self, a: int, b: int) -> int:
        return int(a / b)
