class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        reversed_num = nums.copy()
        reversed_num.reverse()
        left_dp = [0]*(firstLen-1)
        right_dp = [0]*(firstLen-1)
        right_current_sum = sum(reversed_num[:firstLen])
        current_sum = sum(nums[:firstLen])
        left_dp.append(current_sum)
        right_dp.append(right_current_sum)
        for i in range(firstLen, len(nums)):
            current_sum += nums[i]-nums[i-firstLen]
            left_dp.append(max(current_sum, left_dp[-1]))
            right_current_sum += reversed_num[i]-reversed_num[i-firstLen]
            right_dp.append(max(right_current_sum, right_dp[-1]))
        right_dp.reverse()
        #print(left_dp)
        #print(right_dp)
        
        ans = 0
        current_sum = sum(nums[:secondLen])
        if secondLen+1<len(nums):
            ans = current_sum+right_dp[secondLen+1]
        else:
            ans = current_sum
        for i in range(secondLen, len(nums)):
            current_sum += nums[i]-nums[i-secondLen]
            if i+1<len(nums):
                first_possible_sum = max(left_dp[i-secondLen], right_dp[i+1])
            else:
                first_possible_sum = left_dp[i-secondLen]
            ans = max(ans, current_sum+first_possible_sum)
            
        return ans
        
            
        
        
        
