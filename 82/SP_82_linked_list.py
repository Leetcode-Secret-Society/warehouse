# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        resultHead = result = ListNode(0, head) #faaaaster
        # result = ListNode(0, head)
        # resultHead = result
        while node != None:
            print(node.val)
            #searching dup node
            if node.next != None and node.val == node.next.val:
                while node.next != None and node.val == node.next.val:
                    # print(f"{node.val=}")
                    node = node.next
                result.next = node.next
            else: 
                result = result.next
                
            node = node.next
        return resultHead.next
