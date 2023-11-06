# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Seek end to get half
        half_seeker,end_seeker = head, head
        while end_seeker:
            half_seeker = half_seeker.next
            end_seeker = end_seeker.next.next

        # Reverse right half of the linked list.
        rev_curr, rev_prev = half_seeker, None
        while rev_curr:       
            tmp_next = rev_curr.next
            rev_curr.next = rev_prev
            rev_prev = rev_curr
            rev_curr = tmp_next
        
        # Get result
        result = 0
        left,right = head, rev_prev
        while right:
            result = max(left.val + right.val, result)
            left = left.next
            right = right.next
        
        return result
