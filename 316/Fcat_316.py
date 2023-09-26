# Definition for a binary tree node.
from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        s_count = Counter(s)

        stack = []
        selected = set()
        for c in s:
            s_count[c] -= 1
            while stack and c < stack[-1] and c not in selected:
                if s_count[stack[-1]] > 0:
                    selected.remove(stack.pop())
                else:
                    break

            if c not in selected:
                selected.add(c)
                stack.append(c)

        return "".join(stack)

print(Solution().removeDuplicateLetters("abacb"))