class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        counter = 0
        i = 0
        j = 0
        while j < len(s):
            stack.append(s[j])
            if stack[i] == s[j]:
                counter += 1
            else:
                i = len(stack) - 1
                counter = 1

            if counter == k:
                for _ in range(k):
                    stack.pop()
                i = max(0, i-1)
                if stack:
                    counter = 1
                else:
                    counter = 0
                while i != 0 and stack[i] == stack[i-1]:
                    counter += 1
                    i -= 1
            j += 1
        return ''.join(stack)


print(Solution().removeDuplicates('abceetteecba', 2))