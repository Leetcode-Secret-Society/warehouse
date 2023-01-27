from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        def find(index):
            group, _, index = groups[index]
            if group == index:
                return group
            else:
                groups[index][0] = find(group)
                return groups[index][0]

        def merge(index1, index2):
            group1 = find(index1)
            group2 = find(index2)
            if group1 == group2:
                return
            groups[group2][0] = group1
            groups[group1][1] += groups[group2][1]
            self.max_group_size = max(self.max_group_size, groups[group1][1])

        self.max_group_size = 1
        groups = {}
        for num in nums:
            groups[num] = [num, 1, num]

        for n in groups.keys():
            if n + 1 in groups:
                merge(n, n + 1)
            if n - 1 in groups:
                merge(n, n - 1)

        return self.max_group_size
