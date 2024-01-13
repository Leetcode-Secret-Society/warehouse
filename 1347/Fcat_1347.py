class Solution:
    def minSteps(self, s: str, t: str) -> int:
        char_count_s = [0] * 26
        for c in s:
            char_count_s[ord(c) - ord("a")] += 1

        for c in t:
            c_index = ord(c) - ord("a")
            if char_count_s[c_index] > 0:
                char_count_s[c_index] -= 1

        return sum(char_count_s)
