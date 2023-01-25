from typing import List


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        children = [[] for _ in range(len(parent))]
        for i, p in enumerate(parent):
            if p == -1:
                root = i
            else:
                children[p].append(i)

        def find_longest_child_path(node):
            first = 0
            second = 0
            for child in children[node]:
                cur = find_longest_child_path(child)
                if cur > first:
                    second = first
                    first = cur
                elif cur > second:
                    second = cur

            if children[node]:
                self.longest_path = max(self.longest_path, first + second + 1)
            if s[parent[node]] != s[node]:
                return first+1
            else:
                return 0

        self.longest_path = 1
        find_longest_child_path(root)
        return self.longest_path
