from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        index_map = {}
        current_len = 0
        result = 0
        for i, n in enumerate(nums):
            if n in index_map:
                for j in range(i-current_len, index_map[n]):
                    total -= nums[j]
                    del index_map[nums[j]]
                    current_len -= 1
                index_map[n] = i
            else:
                current_len += 1
                index_map[n] = i
                total += n
                if current_len == k:
                    result = max(result, total)
                    total -= nums[i-k+1]
                    del index_map[nums[i-k+1]]
                    current_len -= 1
        return result

print(Solution().maximumSubarraySum([3,2,3,1],3))