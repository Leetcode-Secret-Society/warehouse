class Solution:
    def countVowelPermutation(self, n: int) -> int:
        last_a = 1
        last_e = 1
        last_i = 1
        last_o = 1
        last_u = 1
        for _ in range(1, n):
            a = last_e + last_i + last_u
            e = last_a + last_i
            i = last_e + last_o
            o = last_i
            u = last_i + last_o
            last_a = a
            last_e = e
            last_i = i
            last_o = o
            last_u = u
        return (last_a + last_e + last_i + last_o + last_u) % (10**9+7)