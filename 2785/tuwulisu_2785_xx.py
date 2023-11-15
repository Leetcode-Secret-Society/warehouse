class Solution:
    def sortVowels(self, s: str) -> str:
        vowel_counter = defaultdict(int)
        vowel_order = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
        vowel_set = set(vowel_order)
        t = []
        vowel_indexes = []
        for i, c in enumerate(s):
            if c in vowel_set:
                t.append('')
                vowel_indexes.append(i)
                vowel_counter[c] += 1
            else:
                t.append(c)
        i = 0
        for vowel in vowel_order:
            while vowel in vowel_counter and vowel_counter[vowel] > 0:
                t[vowel_indexes[i]] = vowel
                vowel_counter[vowel] -= 1
                i += 1
        return "".join(t)
        
