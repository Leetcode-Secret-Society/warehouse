class Solution:
    def reorganizeString(self, s: str) -> str:
        char_count = [0] * 26
        for c in s:
            char_count[ord(c) - 97] += 1

        max_index = 0
        max_char_count = 0
        for i in range(26):
            if char_count[i] > max_char_count:
                max_index = i
                max_char_count = char_count[i]
        if max_char_count > len(s) - max_char_count + 1:
            return ""

        result_list = [chr(max_index+97)] * max_char_count
        char_count[max_index] = 0
        j = 0
        for i in range(26):
            for c in range(char_count[i]):
                result_list[j] += chr(i+97)
                j += 1
                j %= max_char_count

        return "".join(result_list)
