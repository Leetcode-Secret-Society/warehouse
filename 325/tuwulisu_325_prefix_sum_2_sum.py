class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix_sum_length_dict = {0: 0}
        prefix_sum = 0
        for i, n in enumerate(nums):
            prefix_sum+=n
            if prefix_sum not in prefix_sum_length_dict:
                prefix_sum_length_dict[prefix_sum]=i+1
        #print(prefix_sum_length_dict)
        suffix_sum = 0
        sum_of_nums = sum(nums)
        #print(sum_of_nums)
        max_length = 0
        for i, n in enumerate(reversed(nums)):
            suffix_length = i
            if sum_of_nums - suffix_sum - k in prefix_sum_length_dict:
                max_length = max(max_length, len(nums) - suffix_length - prefix_sum_length_dict[sum_of_nums - suffix_sum - k])
            suffix_sum+=n
        return max_length
