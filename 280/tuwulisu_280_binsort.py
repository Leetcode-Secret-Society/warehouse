class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = defaultdict(int)
        min_n = float('inf')
        max_n = float('-inf')
        for n in nums:
            counter[n]+=1
            min_n = min(n, min_n)
            max_n = max(n, max_n)
        curr_min = min_n
        curr_max = max_n
        for i in range(len(nums)):
            if i%2==0:
                nums[i] = curr_min
                counter[curr_min]-=1
                while counter[curr_min]==0 and curr_min < max_n:
                    curr_min+=1
            else:
                nums[i] = curr_max
                counter[curr_max]-=1
                while counter[curr_max]==0 and curr_max > min_n:
                    curr_max-=1

                
            
