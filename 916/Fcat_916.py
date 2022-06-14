from typing import List
from collections import Counter, defaultdict


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        words2_union = defaultdict(int)
        for word2 in words2:
            word2_counter = Counter(word2)
            for char in word2_counter:
                words2_union[char] = max(words2_union[char], word2_counter[char])
        result = []
        for word in words1:
            word_counter = Counter(word)
            for char in words2_union:
                if word_counter.get(char, 0) < words2_union[char]:
                    break
            else:
                result.append(word)
        return result
