class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        result = ''
        for index in range(len(s)):
            if s[index] == '(':
                stack.append(len(result))
            elif s[index] == ')':
                if stack:
                    stack.pop()
                else:
                    continue
            result += (s[index])
        for i in stack[::-1]:
            result = result[:i] + result[i+1:]
        return result
            