from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        cur_score = 0
        max_score = 0
        left = 0
        right = len(tokens) - 1
        while left <= right:
            if power < tokens[left]:
                if cur_score == 0:
                    break
                cur_score -= 1
                power += tokens[right]
                right -= 1
            else:
                cur_score += 1
                max_score = max(max_score, cur_score)
                power -= tokens[left]
                left += 1

        return max_score
