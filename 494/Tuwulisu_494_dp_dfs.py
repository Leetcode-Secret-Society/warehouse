class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dict_=dict()
        
        def dfs(layer_id: int, nums: List[int], current_num: int, target: int)->int:
            if layer_id >= len(nums):
                if current_num==target:
                    return 1
                else:
                    return 0
            if layer_id in dict_ and current_num in dict_[layer_id]:
                return dict_[layer_id][current_num]
            plus_outcome = dfs(layer_id+1, nums, current_num+nums[layer_id], target)
            minus_outcome = dfs(layer_id+1, nums, current_num-nums[layer_id], target)
            if layer_id not in dict_:
                dict_[layer_id]=dict()
            dict_[layer_id][current_num] = plus_outcome + minus_outcome
            return plus_outcome + minus_outcome
        
        return dfs(0,nums,0,target)
