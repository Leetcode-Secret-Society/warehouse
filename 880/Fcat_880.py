
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        total_size = 0
        for c in s:
            if c.isnumeric():
                total_size *= int(c)
            else:
                total_size += 1

        for i in range(len(s)-1,-1,-1):
            k %= total_size

            if k == 0 and s[i].isalpha():
                return s[i]

            if s[i].isnumeric():
                total_size /= int(s[i])
            else:
                total_size -= 1





