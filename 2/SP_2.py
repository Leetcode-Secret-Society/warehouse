# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: 
        decimal_shift = 0
        curr_l1 = l1
        curr_l2 = l2
        result_node = ListNode()
        head = result_node
        while curr_l1 != None or curr_l2 != None or decimal_shift != 0:
            result_node.next = ListNode()
            result_node = result_node.next
            result = getattr(curr_l1, 'val' , 0) + getattr(curr_l2, 'val' , 0) + decimal_shift
            if result >= 10:
                decimal_shift = 1
                result -= 10
            else :
                decimal_shift = 0
            # print(f"{result=} {decimal_shift=}")
            result_node.val = result
            if curr_l1 != None:
                curr_l1 = curr_l1.next
            if curr_l2 != None:
                curr_l2 = curr_l2.next

        return head.next
