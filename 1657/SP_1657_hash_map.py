class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        dic_1 = collections.defaultdict(lambda: 0)
        dic_2 = collections.defaultdict(lambda: 0)
        for c in word1:
            dic_1[c] += 1
        for c in word2:
            dic_2[c] += 1
    
        return set(word1) == set(word2) and sorted(list(dic_1.values())) == sorted(list(dic_2.values()))
