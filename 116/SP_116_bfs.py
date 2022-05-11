
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
        

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        node = root
        while node and node.left:#search horizontal level
            print("*"+str(node.val))
            next = node.left
            while node: #search parrell level
                print(node.val)
                node.left.next = node.right
                node.right.next = node.next and node.next.left #return node.next.left if both exist
                node = node.next
            node = next
        return root
