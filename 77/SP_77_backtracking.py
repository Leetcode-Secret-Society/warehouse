class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = list()
        def backtrack(start: int, combination:List[int]) :
            if len(combination) == k:
                # print(combination)
                result.append(combination.copy())
            for i in range(start, n+1):
                combination.append(i)
                # print(f"{start=} {i=} {combination=}")
                backtrack(i + 1, combination)
                combination.pop()
                # print(combination.pop())
                
        backtrack(1, [])
        return result
