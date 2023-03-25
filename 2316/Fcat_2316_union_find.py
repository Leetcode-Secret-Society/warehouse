from typing import List


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        def find(i):
            group = groups[i][0]
            if group == i:
                return i
            else:
                groups[i][0] = find(group)
                return groups[i][0]

        def merge(node1, node2):
            group1 = find(node1)
            group2 = find(node2)
            if group1 == group2:
                return

            merged_size = groups[group1][1] + groups[group2][1]
            groups[group2] = [group1, merged_size]
            groups[group1][1] = merged_size

        groups = [[i, 1] for i in range(n)]

        for start, end in edges:
            merge(start, end)
        all_group_size = []
        for i in range(n):
            group, size = groups[i]
            if i != group:
                continue
            all_group_size.append(size)

        result = 0
        current_node_nums = all_group_size[0]
        for i in range(1, len(all_group_size)):
            result += current_node_nums * all_group_size[i]
            current_node_nums += all_group_size[i]
        return result
