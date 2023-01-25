class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        node1_seen = set()
        node2_seen = set()
        while (node1!=-1 and node1 not in node1_seen) or (node2!=-1 and node2 not in node2_seen):
            if node1==node2:
                return node1
            possible_nodes = []
            if node1 in node2_seen:
                possible_nodes.append(node1)
            if node2 in node1_seen:
                possible_nodes.append(node2)
            if possible_nodes:
                return min(possible_nodes)
            if node1!=-1 and node1 not in node1_seen:
                node1_seen.add(node1)
                node1 = edges[node1]
            if node2!=-1 and node2 not in node2_seen:
                node2_seen.add(node2)
                node2 = edges[node2]
        return -1
