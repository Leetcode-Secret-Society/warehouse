class Solution:
    def numberOfWays(self, s: str) -> int:
        left_zeros = 0 if s[0] == '1' else 1
        left_ones = 1 - left_zeros
        right_zeros = 0
        for i in range(1, len(s)):
            if s[i] == '0':
                right_zeros += 1
        right_ones = len(s) - 1 - right_zeros
        result = 0
        for i in range(1, len(s) - 1):
            if s[i] == '1':
                right_ones -= 1
                left_ones += 1
                result += left_zeros * right_zeros
            else:
                right_zeros -= 1
                left_zeros += 1
                result += left_ones * right_ones

        return result


print(Solution().numberOfWays("001101"))
