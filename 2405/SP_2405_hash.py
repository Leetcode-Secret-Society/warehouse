class Solution:
    def partitionString(self, s: str) -> int:
        tmp = set()
        count = 0
        for char in s:
            if char in tmp:
                tmp.clear()
                count += 1
            tmp.add(char)
        return count + 1
