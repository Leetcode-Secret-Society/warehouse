from typing import List


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        next_candle_to_right = -1
        next_candle_to_right_memo = [-1] * len(s)
        candle_prefix_sum = [0]
        candle_count = 0
        for i in range(len(s)):
            if s[i] == '|':
                next_candle_to_right = i
                candle_count += 1
            next_candle_to_right_memo[i] = next_candle_to_right
            candle_prefix_sum.append(candle_count)
        next_candle_to_left = -1
        next_candle_to_left_memo =[-1] * len(s)
        for i in range(len(s)-1,-1,-1):
            if s[i] == '|':
                next_candle_to_left = i
            next_candle_to_left_memo[i] = next_candle_to_left

        result = []
        for query in queries:
            left_candle = next_candle_to_left_memo[query[0]]
            right_candle = next_candle_to_right_memo[query[1]]
            if left_candle >= query[1] or right_candle <= query[0] or right_candle == left_candle:
                result.append(0)
            else:
                result.append(right_candle - left_candle + 1 - (candle_prefix_sum[right_candle+1] - candle_prefix_sum[left_candle]))
        return result

print(Solution().platesBetweenCandles("***|**|*****|**||**|*", [[1,17],[4,5],[14,17],[5,11],[15,16]]))


