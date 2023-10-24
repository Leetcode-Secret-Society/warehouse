from typing import List
from collections import defaultdict

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        user_pattern = defaultdict(list)
        for i in range(len(username)):
            user_pattern[username[i]].append((timestamp[i], website[i]))

        pattern_scores = defaultdict(int)
        max_score = 0
        for value in user_pattern.values():
            value.sort()
            pattern_set = set()
            for i in range(len(value) - 2):
                for j in range(i + 1, len(value) - 1):
                    for k in range(j + 1, len(value)):
                        pattern = (value[i][1], value[j][1], value[k][1])
                        if pattern in pattern_set:
                            continue
                        pattern_scores[pattern] += 1
                        max_score = max(max_score, pattern_scores[pattern])
                        pattern_set.add(pattern)

        result = []
        for key, value in pattern_scores.items():
            if value == max_score:
                result.append(key)
        result.sort()
        return list(result[0])