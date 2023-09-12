from collections import defaultdict


class Solution:
    def minDeletions(self, s: str) -> int:
        counts = [0] * 26
        for c in s:
            counts[ord(c)-97] += 1
        frequency_mapping = defaultdict(list)
        for i in range(26):
            frequency_mapping[counts[i]].append(chr(i+97))

        max_frequency = max(counts)
        moves = 0
        for f in range(max_frequency, 0,-1):
            while len(frequency_mapping[f]) > 1:
                moves += 1
                frequency_mapping[f-1].append(frequency_mapping[f].pop())

        return moves



