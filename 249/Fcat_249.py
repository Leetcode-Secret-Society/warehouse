from typing import List
import string
from collections import defaultdict

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        alphabet_num_mapping = {}
        group_mapping = defaultdict(list)
        for i, alphabet in enumerate(string.ascii_lowercase):
            alphabet_num_mapping[alphabet] = i

        for s in strings:
            gap = ""
            for i in range(len(s)-1):
                gap += f'{str((alphabet_num_mapping[s[i+1]] - alphabet_num_mapping[s[i]]) % 26)} '
            group_mapping[gap].append(s)

        return group_mapping.values()
