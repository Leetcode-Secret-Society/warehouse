class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count_indice = {0:0}
        current_count = 0
        max_len = 0
        for i, n in enumerate(nums):
            index=i+1
            if n==0:
                current_count-=1
            else:
                current_count+=1
            if current_count in count_indice:
                max_len = max(max_len, index-count_indice[current_count])
            else:
                count_indice[current_count]=index
        return max_len
                
        
