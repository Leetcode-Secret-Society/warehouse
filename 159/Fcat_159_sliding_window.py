class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        last_character_index = {}
        start_index = 0
        result = 0
        for i, c in enumerate(s):
            if len(last_character_index) == 2 and c not in last_character_index:
                pop_key, pop_value = None, len(s)
                for key, value in last_character_index.items():
                    if value < pop_value:
                        pop_key = key
                        pop_value = value
                del last_character_index[pop_key]
                result = max(result, i - start_index)
                start_index = pop_value + 1

            last_character_index[c] = i
        result = max(result, len(s) - start_index)
        return result
