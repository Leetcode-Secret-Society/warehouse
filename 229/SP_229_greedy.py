class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #be noticed that "larger" than n/3, so there would 2 peaks at most
        #find top2 ele
        # [2,1,1,3,1,4,5,6]
        peak = None
        peak_2 = None
        count = 0
        count_2 = 0
        for num in nums:
            if count <= 0 and num != peak_2:
                peak = num
                count += 1
            elif count_2 <= 0 and num != peak:
                peak_2 = num
                count_2 += 1
            elif peak == num:
                count += 1
            elif peak_2 == num:
                count_2 += 1
            else :
                count -= 1
                count_2 -= 1
        
        #filter if not larger than n/3
        result = []
        for p in [peak, peak_2]:
            if nums.count(p) > len(nums) // 3:
                result.append(p)
        return result
