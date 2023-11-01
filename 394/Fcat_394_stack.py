class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        bracket_indexes = []
        for i, c in enumerate(s):
            if c == ']':
                left = bracket_indexes.pop()
                s = stack[left+1:]
                nums = ""
                j = left
                while j >= 1 and str.isdigit(stack[j-1]):
                    nums = stack[j-1] + nums
                    j -= 1
                s *= int(nums)
                stack = stack[:j] + s
            else:
                if c == '[':
                    bracket_indexes.append(len(stack))
                stack.append(c)
        return "".join(stack)
