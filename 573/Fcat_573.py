from typing import List


class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        tree_dists = [0] * len(nuts)
        squirrel_dists = [0] * len(nuts)

        for i, nut in enumerate(nuts):
            tree_dist = abs(nut[0] - tree[0]) + abs(nut[1] - tree[1])
            squirrel_dist = abs(nut[0] - squirrel[0]) + abs(nut[1] - squirrel[1])
            tree_dists[i] = tree_dist
            squirrel_dists[i] = squirrel_dist
        twice_all_tree_dists = sum(tree_dists) * 2
        min_dist = float("inf")
        for i in range(len(nuts)):
            min_dist = min(min_dist, twice_all_tree_dists - tree_dists[i] + squirrel_dists[i])
        return min_dist