class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        current_queue = []
        ans = set()
        def backtrack(i):
            if len(current_queue)>1:
                ans.add(tuple(current_queue))
            if i==n:
                return
            if not current_queue or nums[i]>=current_queue[-1]:
                current_queue.append(nums[i])
                backtrack(i+1)
                current_queue.pop()
            backtrack(i+1)
        backtrack(0)
        return ans
