class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_characters = [0] * 26
        for c in s1:
            s1_characters[ord(c)-97] += 1
        current_alphabets = [0] * 26
        for i in range(len(s1)):
            current_alphabets[ord(s2[i])-97] += 1
        if s1_characters == current_alphabets:
            return True
        for i in range(len(s1), len(s2)):
            current_alphabets[ord(s2[i])-97] += 1
            current_alphabets[ord(s2[i-len(s1)])-97] -= 1
            if s1_characters == current_alphabets:
                return True
        return False
