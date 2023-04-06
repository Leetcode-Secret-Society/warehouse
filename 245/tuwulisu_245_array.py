class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        word1_indexs = []
        word2_indexs = []
        for i, word in enumerate(wordsDict):
            if word == word1:
                word1_indexs.append(i)
            if word == word2:
                word2_indexs.append(i)
        word2_pos = 0
        word1_pos = 0
        min_distance = float('inf')
        while word1_pos < len(word1_indexs) and word2_pos < len(word2_indexs):
            word1_index = word1_indexs[word1_pos]
            word2_index = word2_indexs[word2_pos]
            if word1_index == word2_index:
                word1_pos+=1
                continue
            min_distance = min(min_distance, abs(word1_index-word2_index))
            if word1_index < word2_index:
                word1_pos+=1
            else:
                word2_pos+=1
        return min_distance
        
