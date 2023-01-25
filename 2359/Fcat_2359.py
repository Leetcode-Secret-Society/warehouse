from typing import List


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        record1 = set()
        record2 = set()
        result = -1
        while node1 != -1 or node2 != -1:
            if node1 != -1 and node1 not in record1:
                record1.add(node1)
                if node1 in record2:
                    result = node1
                node1 = edges[node1]
            else:
                node1 = -1
            if node2 != -1 and node2 not in record2:
                record2.add(node2)
                if node2 in record1:
                    if result == -1 or result > node2:
                        result = node2
                node2 = edges[node2]
            else:
                node2 = -1
            if result != -1:
                return result
        return result

