class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        #copied from 713
        left = 0
        summ = 0
        result = math.inf
        for right in range(len(nums)):
            # total += nums[right]
            summ += nums[right]
            # print(f"{left=} {right=} {summ=} {result=}")
            while summ >= target:
                if summ >= target:
                    result = min(result, right - left + 1)
                summ -= nums[left]
                left += 1
                # print(f"inner {left=} {right=} {summ=} {result=}")
            if summ >= target:
                result = min(result, right - left + 1)
        if result == math.inf:
            return 0
        
        return result
