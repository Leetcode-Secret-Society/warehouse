from typing import List
from collections import defaultdict, Counter


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)

        for s in strs:
            temp = [0] * 26
            c_count = Counter(s)
            for c, count in c_count.items():
                temp[ord(c)-97] = count
            mapping[tuple(temp)].append(s)

        return list(mapping.values())
