
from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        word_1_char_count = [0] * 26
        word_2_char_count = [0] * 26
        word_1_set = set()
        word_2_set = set()
        for c in word1:
            word_1_char_count[ord(c)-ord("a")] += 1
            word_1_set.add(c)

        for c in word2:
            word_2_char_count[ord(c)-ord("a")] += 1
            word_2_set.add(c)
        return word_1_set == word_2_set and Counter(word_1_char_count) == Counter(word_2_char_count)
