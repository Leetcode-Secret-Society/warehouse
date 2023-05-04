from typing import List


class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_length = 0

        for word in words:
            max_length = max(max_length, len(word))
        result = ["" for _ in range(max_length)]
        for i in range(max_length):
            for word in words:
                if i < len(word):
                    result[i] += word[i]
                else:
                    result[i] += " "
        for i in range(max_length):
            result[i] = result[i].rstrip()

        return result

print(Solution().printVertically("TO BE OR NOT TO BE"))