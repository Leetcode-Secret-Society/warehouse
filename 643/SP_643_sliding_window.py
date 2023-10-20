class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) <= k:
            return sum(nums) / k
        current = 0
        result = 0
        for i in range(k):
            current += nums[i]
        result = current
        for i in range(k, len(nums)):
            current += nums[i]
            current -= nums[i - k]
            result = max(result, current)
        return result / k
