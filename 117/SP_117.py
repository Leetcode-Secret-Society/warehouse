class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        node = root
        while node:
            curr = dummy = Node(0) #using dummy to keep next layer head
            while node: #traverse current layer
                if node.left:
                    curr.next = node.left
                    curr = curr.next
                if node.right:
                    curr.next = node.right
                    curr = curr.next
                node = node.next
            node = dummy.next
                
        return root
