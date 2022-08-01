class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candi_copy = candidates.copy()
        visited = set()
        result = set()
        def go(target: int, candi: List[int], start:int, comb: List[int]):
            tup = tuple(comb)
            if (target ,tup) in visited:
                return
            visited.add((target, tup))
            if target == 0:
                result.add(tup)
                return
            elif target < 0:
                return
            for i in range(start,len(candi)):
                comb.append(candi[i])
                go(target - candi[i], candi, i + 1, comb) #sort candidate and push index to prevent dup result, like [1,6,1] / [1,1,6]
                comb.pop()
        go(target,sorted(candidates), 0, [])
        # print(result)
        return result
