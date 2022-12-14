class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        index_dic = dict()
        for index,k_c in enumerate(keyboard):
            index_dic[k_c] = index
        
        step = 0
        current_pos = 0
        for c in word:
            step += abs(current_pos - index_dic[c])
            current_pos = index_dic[c]
        
        return step
