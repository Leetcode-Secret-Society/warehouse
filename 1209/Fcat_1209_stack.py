class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if not stack:
                counter = 0
            stack.append(c)
            counter += 1
            if len(stack) >= 2 and c != stack[-2]:
                counter = 1
            else:
                if counter == k:
                    for _ in range(k):
                        stack.pop()
                    counter = 1
                    check_index = len(stack) - 2
                    while check_index >= 0 and stack[-1] == stack[check_index]:
                        counter += 1
                        check_index -= 1
        return ''.join(stack)


print(Solution().removeDuplicates('pbbcggttciiippooaais', 2))