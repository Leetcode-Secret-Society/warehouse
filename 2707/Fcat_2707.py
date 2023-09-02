from typing import List


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        self.trie = build_trie(dictionary)
        self.dp = [0] * (len(s) + 1)
        self.current_min_extra = 0
        for i in range(len(s)-1,-1,-1):
            self.dp[i] = self.find_min_extra_char(s[i:])

        return self.dp[0]

    def find_min_extra_char(self, s):
        current_dict = self.trie
        min_extra = self.current_min_extra + 1
        possible_extras = []
        for i in range(len(s)):
            c = s[i]
            if c in current_dict:
                current_dict = current_dict[c]
            else:
                break
            if current_dict.get("end", False):
                possible_extras.append(self.dp[len(self.dp)-(len(s)-i)])
        if len(possible_extras) == 0:
            self.current_min_extra += 1
        else:
            min_extra = min(min(possible_extras), min_extra)
            self.current_min_extra = min_extra
        return min_extra

def build_trie(dictionary):
    trie = {}
    for word in dictionary:
        current_dict = trie
        for i in range(len(word)):
            c = word[i]
            if c not in current_dict:
                current_dict[c] = {}
            current_dict = current_dict[c]
            if i == len(word)-1:
                current_dict["end"] = True
    return trie




print(Solution().minExtraChar("leetscode", ["leet","code","leetcode"]))