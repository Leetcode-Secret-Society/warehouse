from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parent = [-1] * n
        for i in range(n):
            if leftChild[i] != -1:
                if parent[leftChild[i]] != -1:
                    return False
                parent[leftChild[i]] = i
            if rightChild[i] != -1:
                if parent[rightChild[i]] != -1:
                    return False
                parent[rightChild[i]] = i
        if parent.count(-1) != 1:
            return False
        traverse_count = 0
        queue = [parent.index(-1)]
        traversed = [False] * n
        while queue:
            index = queue.pop()
            traversed[index] = True
            traverse_count += 1
            left_child = leftChild[index]
            right_child = rightChild[index]
            if left_child != -1 and not traversed[left_child]:
                queue.append(left_child)
            if right_child != -1 and not traversed[right_child]:
                queue.append(right_child)
        if traverse_count != n:
            return False
        return True
