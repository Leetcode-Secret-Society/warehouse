class Solution:
    def appealSum(self, s: str) -> int:
        all_chr_index = [[-1] for _ in range(26)]
        for i, c in enumerate(s):
            all_chr_index[ord(c) - ord('a')].append(i)
        total = 0
        for chr_index in all_chr_index:
            for i in range(1, len(chr_index)):
                total += (len(s) - chr_index[i]) * (chr_index[i] - chr_index[i - 1])

        return total