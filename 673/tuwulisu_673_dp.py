class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        length_at_index = [1]*len(nums)
        option_at_index = [1]*len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length_at_index[j]+1>length_at_index[i]:
                        length_at_index[i]=length_at_index[j]+1
                        option_at_index[i]=option_at_index[j]
                    elif length_at_index[j]+1==length_at_index[i]:
                        option_at_index[i]+=option_at_index[j]
        max_length = max(length_at_index)
        res = 0
        for i, length in enumerate(length_at_index):
            if length == max_length:
                res+=option_at_index[i]
        return res
                    
