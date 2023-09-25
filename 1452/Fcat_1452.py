from typing import List
from collections import defaultdict


class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        company_to_index = defaultdict(set)
        result = []
        for index, companies in enumerate(favoriteCompanies):
            for company in companies:
                company_to_index[company].add(index)

        for index, companies in enumerate(favoriteCompanies):
            parent_candidates = company_to_index[companies[0]]
            for parent_candidate in parent_candidates:
                if parent_candidate == index:
                    continue
                for company in companies:
                    if parent_candidate not in company_to_index[company]:
                        break
                else:
                    break
            else:
                result.append(index)

        return result

print(Solution().peopleIndexes([["leetcode"],["google"],["facebook"],["amazon"]]))