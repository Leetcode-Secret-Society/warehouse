class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        for k in range(len(nums)):
            i = 0
            j = k-1
            while i<j:
                if nums[i]+nums[j]+nums[k] < target:
                    count += j-i
                    i+=1
                else:
                    j-=1
        return count
