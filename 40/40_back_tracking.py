from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        result = set()

        def recursive(cur_result, cur_sum, rest, index):
            if cur_sum + rest < target:
                return
            if cur_sum == target:
                result.add(tuple(cur_result))
            if index >= len(candidates) or cur_sum > target:
                return
            for i in range(index, len(candidates)):
                if i != index and candidates[i] == candidates[i-1]:
                    continue
                cur_result.append(candidates[i])
                recursive(cur_result, cur_sum + candidates[i], rest - candidates[i], i + 1)
                cur_result.pop()

        total = sum(candidates)
        for i in range(len(candidates)):
            if i != 0 and candidates[i] == candidates[i-1]:
                continue
            recursive([candidates[i]], candidates[i], total - candidates[i], i + 1)

        list_result = []

        for comb in result:
            list_result.append(list(comb))
        return list_result
