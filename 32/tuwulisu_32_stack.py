class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        pos_set = set()
        for j, c in enumerate(s):
            if c == '(':
                stack.append(j)
            else:
                if stack:
                    i = stack.pop()
                    pos_set.add(i)
                    pos_set.add(j)
        max_length = 0
        length = 0
        for i in range(len(s)):
            if i in pos_set:
                length+=1
            else:
                max_length = max(max_length, length)
                length=0
        max_length = max(max_length, length)
        return max_length
