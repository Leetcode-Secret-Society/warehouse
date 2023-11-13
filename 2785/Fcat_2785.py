class Solution:
    def sortVowels(self, s: str) -> str:
        vowel_counts = {"A": 0, "E": 0, "I": 0, "O": 0, "U": 0, "a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
        vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
        vowel_indexes = []
        for i, c in enumerate(s):
            if c in vowel_counts:
                vowel_counts[c] += 1
                vowel_indexes.append(i)
        vowel_count_index = 0
        result = list(s)
        for i in vowel_indexes:
            while vowel_counts[vowels[vowel_count_index]] == 0:
                vowel_count_index += 1
            result[i] = vowels[vowel_count_index]
            vowel_counts[vowels[vowel_count_index]] -= 1

        return "".join(result)