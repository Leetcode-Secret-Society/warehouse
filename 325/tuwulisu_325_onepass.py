class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix_sum_length_dict = {0: 0}
        prefix_sum = 0
        max_length = 0
        for i, n in enumerate(nums):
            prefix_sum+=n
            if prefix_sum not in prefix_sum_length_dict:
                prefix_sum_length_dict[prefix_sum]=i+1
            if prefix_sum-k in prefix_sum_length_dict:
                max_length=max(max_length, i+1 - prefix_sum_length_dict[prefix_sum-k])
        
        return max_length
