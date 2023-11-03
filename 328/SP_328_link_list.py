# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        odd_node = head
        original_even_node = head.next
        even_node = head.next
        while odd_node.next and even_node.next :
            odd_node.next = odd_node.next.next
            odd_node = odd_node.next
            even_node.next = even_node.next.next
            even_node = even_node.next

        odd_node.next = original_even_node

        return head
