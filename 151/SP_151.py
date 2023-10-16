#easy in python, no need trimming
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))
