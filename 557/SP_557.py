class Solution:
    def reverseString(left: int, right: int, s: List[str]) -> None:
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    def reverseWords(self, s: str) -> str:
        left = 0
        right = 0
        stringList = list(s)
        for index, charac in enumerate(stringList):
            if charac == ' ':
                right = index - 1
                Solution.reverseString(left, right, stringList)
                left = index + 1
        right = len(s) -1
        Solution.reverseString(left, right, stringList)
        return "".join(stringList)
