class Solution:
    def countTheNumOfKFreeSubsets(self, nums: List[int], k: int) -> int:
        #build chart for n elements having x combinations.
        chart = [0] * (len(nums) + 2) #prevent out of range
        #for example, k = 1
        chart[0] = 1 # [1] = {1}
        chart[1] = 2 # [1,2] = {1}, {2}
        #chart[2] = [1,2,3] = [1,2] or [1][3]
        #  {1},{2},{1,3}     {1},{2}    {1,[3]},{[3]}
        #         = dp[1] + (dp[0] + 1)
        #chart[3] = [1,2,3,4] = [1,2,3] + [1,2][4]
        #{1},{2},{3},{4}      {1},{2},{3}  {1,[4]} {2,{4}}
        #{1,3} {1,4} {2,4}       {1,3}       {[4]}
        #{1,4}
        for i in range(2,len(nums)):
            chart[i] = 1 + chart[i-1] + chart[i-2]
        
        nums.sort() #sort to make num or says key being increasing
        groups, group_map = [], {}

        for num in nums:
            # due nums are sorted, 
            # like 5,4,1,3,2 -> 1,2,3,4,5 ; k=2 ; 1->3->5, 2->4
            if num - k in group_map: 
                group_map[num - k].append(num)
                #update dict key to larger one
                group_map[num] = group_map.pop(num - k) 
            else:
                group_map[num] = [num]
                groups.append(group_map[num])
        # print(groups)
        result = []
        #get group combinations
        for group in groups:
            result.append(chart[len(group)-1] + 1) #add empty one {}
        # print(result)
        
        return functools.reduce(lambda x,y: x * y, result)

        
