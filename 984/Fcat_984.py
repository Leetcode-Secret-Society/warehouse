class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        short, long = ('b', 'a') if a > b else ('a', 'b')

        if short == 'a':
            word = 'ba'
            left = b - a
            pair = a
        else:
            word = 'ab'
            left = a - b
            pair = b
        result = ''
        for i in range(pair):
            if left:
                left -=1
                result += long
            result += word
        if left:
            result += long * left
        return result

print(Solution().strWithout3a3b(5,10))