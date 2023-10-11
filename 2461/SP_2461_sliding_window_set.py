class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        s = set()
        current_sum = 0
        result = 0
        left = 0
        for right in range(len(nums)):
            while nums[right] in s or len(s) == k:
                s.remove(nums[left])
                current_sum -= nums[left]
                left += 1

            s.add(nums[right])
            current_sum += nums[right]
            if len(s) == k:
                result = max(current_sum, result)
        return result
