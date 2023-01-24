class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for k in range(len(nums)):
            i=0
            j=k-1
            while i<j:
                two_side = nums[i]+nums[j]
                if two_side > nums[k]:
                    count+=j-i
                    j-=1
                else:
                    i+=1
        return count
