from collections import defaultdict
from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        age_scores_dict = defaultdict(list)
        for i in range(len(ages)):
            age_scores_dict[ages[i]].append(scores[i])

        age_list = list(age_scores_dict.keys())
        age_list.sort()

        sorted_scores = list(set(scores))
        sorted_scores.sort()
        for age in age_list:
            age_scores_dict[age].sort()

        dp = [0] * (len(sorted_scores)+1)
        for age in age_list:
            i = 1
            j = 0
            age_scores_list = age_scores_dict[age]
            while i < len(dp):
                total = 0
                while j < len(age_scores_list) and age_scores_list[j] == sorted_scores[i-1]:
                    total += age_scores_list[j]
                    j += 1
                dp[i] = max(total + dp[i], total + dp[i-1])
                i += 1

        return dp[-1]

print(Solution().bestTeamScore([596,277,897,622,500,299,34,536,797,32,264,948,645,537,83,589,770], [18,52,60,79,72,28,81,33,96,15,18,5,17,96,57,72,72]))