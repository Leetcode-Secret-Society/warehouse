from typing import List


class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        dic = {}
        max_word_length = 0
        for word in words:
            temp_dic = dic
            max_word_length = max(len(word), max_word_length)
            for i in range(len(word)):
                if word[i] not in temp_dic:
                    temp_dic[word[i]] = {}
                temp_dic = temp_dic[word[i]]
                if i == len(word) - 1:
                    temp_dic["hit"] = True
        result = ""

        def find_word(index):
            temp_dic = dic
            end = None
            while index < len(s) and s[index] in temp_dic:
                temp_dic = temp_dic[s[index]]
                if "hit" in temp_dic:
                    end = index

                index += 1
            return end
        i = 0
        while i < len(s):
            end = find_word(i)
            if end is not None:
                start = i
                j = end + 1
                while max(0, end - max_word_length+1) < j:
                    new_end = find_word(j)
                    if new_end is not None and new_end > end:
                        end = new_end
                        j = new_end + 1
                    else:
                        j -= 1

                result += "<b>" + s[start:end+1] + "</b>"
                i = end
                start = end = None
            else:
                result += s[i]

            i+=1
        return result

print(Solution().addBoldTag("aaabbb", ["aa","b"]))