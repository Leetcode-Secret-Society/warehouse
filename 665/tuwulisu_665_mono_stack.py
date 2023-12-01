class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        stack = []
        count=0
        for n in nums:
            while stack and stack[-1]>n:
                stack.pop()
                count+=1
                if count>1:
                    break
            stack.append(n)
        if count<=1:
            return True
        
        stack = []
        count=0
        for n in reversed(nums):
            while stack and stack[-1]<n:
                stack.pop()
                count+=1
                if count>1:
                    return False
            stack.append(n)
        return True
