class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        recorded_seq_list = [dict() for _ in nums]
        max_length = 0
        for i, n in enumerate(nums):
            for j in range(i):
                m = nums[j]
                if n - m in recorded_seq_list[j]:
                    recorded_seq_list[i][n-m]=recorded_seq_list[j][n-m]+1
                else:
                    recorded_seq_list[i][n-m]=2
                max_length = max(max_length, recorded_seq_list[i][n-m])
        
        return max_length
                
