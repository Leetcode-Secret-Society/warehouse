class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = set()
        
        def backtrack(comb: List[int], candidates: List[int]):
            if len(comb) == len(nums):
                result.add(tuple(comb))
                return
            for candidate in candidates:
                comb.append(candidate)
                temp = candidates.copy()
                temp.remove(candidate)
                backtrack(comb, temp)
                comb.pop()
        backtrack([],nums)
        return list(result)
