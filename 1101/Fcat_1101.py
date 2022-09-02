from typing import List


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        groups = [None] * n
        logs.sort(key=lambda x:x[0])
        for timestamp, a, b in logs:
            group_a = set((a,)) if groups[a] is None else groups[a]
            group_b = set((b,)) if groups[b] is None else groups[b]
            new_group = group_a.union(group_b)
            if len(new_group) == n:
                break
            for i in new_group:
                groups[i] = new_group
        else:
            return -1
        return timestamp