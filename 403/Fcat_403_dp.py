# Definition for a binary tree node.
from typing import List
from collections import defaultdict

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        steps = defaultdict(set)
        steps[1].add(1)
        stone_set = set(stones)
        for stone in stones:
            for step in steps[stone]:
                next_move = step + stone
                if next_move + 1 in stone_set:
                    steps[next_move + 1].add(step + 1)
                if next_move in stone_set:
                    steps[next_move].add(step)
                if step - 1 > 0 and next_move - 1 in stone_set:
                    steps[next_move - 1].add(step - 1)

        return bool(steps[stones[-1]])
