# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_mid(self, node: ListNode) -> Tuple[ListNode, ListNode]:
        prev = None
        fast = node
        slow = node
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        return prev, slow
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        if head.next is None:
            return TreeNode(head.val)
        prev, mid = self.get_mid(head)
        prev.next = None
        root = TreeNode(mid.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        return root
