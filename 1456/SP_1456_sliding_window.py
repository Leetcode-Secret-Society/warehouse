class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        count = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1
        result = count
        for i in range(k,len(s)):
            if s[i] in vowels:
                count += 1
            if s[i-k] in vowels:
                count -= 1
            result = max(count, result)
        
        return result
