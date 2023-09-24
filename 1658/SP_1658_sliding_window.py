#revered version of 209
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        l, r, leng = 0,0,len(nums)
        nums.append(0)
        rest_sum = sum(nums) - x
        current = 0
        result = -1
        count = 0
        # [5,2,3] len(3)
        # [] r:0
        # [5] r:1
        # [] r:1
        # [2] r:2
        # [2,3] r:3 --> out of bounds

        while r >= l and r <= len(nums):
            # print(" l:"+str(l)+" r:"+str(r)+" cur:"+str(current)+" len:"+str(len(nums)))
            if current < rest_sum:
                current += nums[r]
                r += 1
                count += 1
            else:
                if current == rest_sum:
                    result = max(count, result)
                current -= nums[l]
                l += 1
                count -= 1

        if result == -1:
            return -1

        return leng - result

