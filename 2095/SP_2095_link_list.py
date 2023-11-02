
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        node = head
        stack = []
        while node.next: 
            stack.append(node)
            node = node.next
        half = (len(stack) - 1) // 2
        # print(stack[half].val)
        stack[half].next = stack[half].next.next
        return head

#constant memory(1)
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        node = head
        end_seeker = head.next.next
        while end_seeker and end_seeker.next: 
            node = node.next
            end_seeker = end_seeker.next.next
        node.next = node.next.next
        return head
