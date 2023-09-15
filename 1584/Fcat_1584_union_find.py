from typing import List
from collections import defaultdict


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0
        distances_map = defaultdict(list)
        for i in range(len(points)-1):
            for j in range(i+1, len(points)):
                distances_map[abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])].append((i,j))

        distances = list(distances_map.keys())
        distances.sort()

        groups = [[i,1] for i in range(len(points))]

        def find(g):
            group = groups[g][0]
            if group == g:
                return g
            groups[g][0] = find(group)
            return groups[g][0]

        def merge(group1, group2):
            group1 = find(group1)
            group2 = find(group2)
            if group1 != group2:
                merged_size = groups[group1][1] + groups[group2][1]
                groups[group1][1] = merged_size
                groups[group2] = [group1, merged_size]
                return True
            return False

        total_distance = 0
        for d in distances:
            for e in distances_map[d]:
                if merge(e[0], e[1]):
                    total_distance += d
                    if groups[find(e[0])][1] == len(points):
                        return total_distance

Solution().minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]])
