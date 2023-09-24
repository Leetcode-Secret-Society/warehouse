from typing import List


class Solution:
    def minSwaps(self, data: List[int]) -> int:
        total = sum(data)
        cur_sum = sum(data[:total])
        result = total
        for j in range(total, len(data)):
            result = min(result, total - cur_sum)
            cur_sum += data[j]
            cur_sum -= data[j-total]
        result = min(result, total - cur_sum)

        return result
