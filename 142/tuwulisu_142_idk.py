# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_map = {}
        node = head
        while node:
            if id(node) in node_map:
                return node_map[id(node)]
            node_map[id(node)] = node
            node=node.next
        return None
