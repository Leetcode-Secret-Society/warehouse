class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        self.add_parent(head, None)
        index = 1
        cur = head
        start = None
        end = None
        while cur:
            if index == left:
                start = cur
            if index == right:
                end = cur
                parent = cur.parent
                cur.parent = cur.next
                cur.next = parent
                if start.next is not None:
                    start.next.next = end
                start.next = end.parent
                break
            if start is not None:
                parent = cur.parent
                cur.parent = cur.next
                cur.next = parent
                cur = cur.parent
            else:
                cur = cur.next
            index += 1
        if left == 1:
            return end
        else:
            return head

    def add_parent(self, node, parent):
        if node.next is not None:
            self.add_parent(node.next, node)
        node.parent = parent

