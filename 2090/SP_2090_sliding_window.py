#a little diff from 643
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        kk = k*2+1
        if len(nums) < kk:
            return [-1] * len(nums)
        current = 0
        result = [-1] * k
        for i in range(kk):
            current += nums[i]
        result.append(current//kk)
        for i in range(kk, len(nums)):
            current += nums[i]
            current -= nums[i - kk]
            result.append(current//kk)
        result.extend([-1] * k)
        return result
