# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        nodeToRemove = head
        counter = 0
        listSize = 0
        while node != None:
            node = node.next
            listSize += 1
            if counter <= n:
                counter += 1
            else:
                nodeToRemove = nodeToRemove.next
        # print(nodeToRemove.val)
        if listSize == n:
            return head.next
        elif nodeToRemove.next:
            nodeToRemove.next = nodeToRemove.next.next
        else:
            return None
        return head
