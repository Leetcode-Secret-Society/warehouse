class Solution:
    def sumGame(self, num: str) -> bool:
        left_q = 0
        right_q = 0
        left = 0
        right = 0
        for i in range(len(num)//2):
            if num[i] == "?":
                left_q += 1
            else:
                left += int(num[i])
        for i in range(len(num)//2, len(num)):
            if num[i] == "?":
                right_q += 1
            else:
                right += int(num[i])

        if (left_q+right_q) % 2 == 1:
            return True
        if left_q > right_q:
            if (right - left) / (left_q -right_q) == 4.5:
                return False
        elif left_q == right_q:
            if left == right:
                return False
        else:
            if (left - right) / (right_q -left_q) == 4.5:
                return False

        return True
print(Solution().sumGame("5023"))