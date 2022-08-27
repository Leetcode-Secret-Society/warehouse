# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.
import math


class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        def recursive_print(node, size):
            if node and size:
                recursive_print(node.getNext(), size - 1)
                node.printValue()

        link_length = 0
        cur = head
        while cur:
            cur = cur.getNext()
            link_length += 1
        heads = []
        block_size = math.ceil(math.sqrt(link_length))
        cur = head
        for _ in range(block_size):
            heads.append(cur)
            for _ in range(block_size):
                if cur:
                    cur = cur.getNext()

        for i in range(len(heads) - 1, -1, -1):
            recursive_print(heads[i], block_size)
