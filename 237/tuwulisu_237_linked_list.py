# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        prev_node = None
        while node:
            if node.next:
                node.val = node.next.val
            else:
                prev_node.next = None
            prev_node = node
            node = node.next


                
