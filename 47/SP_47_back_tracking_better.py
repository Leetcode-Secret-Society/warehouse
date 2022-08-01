class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = set()
        
        def backtrack(comb: List[int], counter):
            if len(comb) == len(nums):
                result.add(tuple(comb))
                return
            for candidate in counter:
            # for candidate in nums: #using nums will leading TLE
                if counter[candidate] > 0:
                    comb.append(candidate)
                    counter[candidate] -= 1
                    backtrack(comb, counter)
                    comb.pop()
                    counter[candidate] += 1
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        backtrack([],counter)
        return list(result)
