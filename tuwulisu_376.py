class Solution:
    def get_max_len(self, nums, is_up):
        l = 1
        for i in range(len(nums)-1):
            if is_up:
                if nums[i]<=nums[i+1]:
                    continue
                else:
                    l+=1
                    is_up=False
            else:
                if nums[i]>=nums[i+1]:
                    continue
                else:
                    l+=1
                    is_up=True
        return l
    def wiggleMaxLength(self, nums: List[int]) -> int:
        return max(self.get_max_len(nums, True), self.get_max_len(nums, False))
