class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: # 0 or 1 cannot be divide by int into smaller one
            return 0
        left = 0
        product = 1
        result = 0
        for right in range(len(nums)):
            product *= nums[right]
            # print(f"{left=} {right=} {product=} {result=}")
            while product >= k:
                product //= nums[left]
                left += 1
                # print(f"inner {left=} {right=} {product=} {result=}")
            result += right - left + 1 #sliding window for counting possbile result
        return result
