class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = set()
        def backtracking(current: List[int], start: int):
            result.add(tuple(current))
            if len(current) == len(nums):
                return
            for ele in range(start,len(nums)):
                current.append(nums[ele])
                backtracking(current, ele + 1)
                current.pop()
        backtracking([],0)
        return result
