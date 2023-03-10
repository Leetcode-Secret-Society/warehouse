# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        node_in_reservoir = self.head
        nth_node = 1
        curr_node = self.head.next
        while curr_node:
            if random.randint(0, nth_node) == 0:
                node_in_reservoir = curr_node
            nth_node+=1
            curr_node = curr_node.next
        return node_in_reservoir.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
