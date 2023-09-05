
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        old_node_map = {}
        cur = head
        while cur is not None:
            node = Node(cur.val, cur.next, cur.random)
            old_node_map[cur] = node
            cur = cur.next

        new_head = old_node_map[head]
        cur = new_head
        while cur is not None:
            if cur.next is not None:
                cur.next = old_node_map[cur.next]
            if cur.random is not None:
                cur.random = old_node_map[cur.random]
            cur = cur.next

        return new_head