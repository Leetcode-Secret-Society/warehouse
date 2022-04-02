class Node:
    def __init__(self, n):
        self.parent = self
        self.n = n
        self.rank = 0
        self.count = 1
        self.visited = False
    def is_root(self):
        return self is self.parent
    def find_root(self):
        if self.is_root():
            return self
        else:
            self.parent = self.parent.find_root()
            return self.parent
    def merge(self, node):
        if self.rank >= node.rank:
            if self.rank==node.rank:
                self.rank+=1
            node.parent = self.find_root()
            self.count+=node.count
        else:
            self.parent = node.find_root()
            node.count+=self.count
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        node_dict = {k: Node(k) for k in range(n)}
        max_size=0
        for i in range(n):
            root = node_dict[i]
            if root.is_root():
                root.visited = True
                node = node_dict[nums[root.n]]
                while not node.visited:
                    node.visited=True
                    root.merge(node)
                    root=root.find_root()
                    node = node_dict[nums[node.n]]
                if node.find_root() is not root:
                    root.merge(node)
                    root=root.find_root()
                max_size = max(max_size, root.count)


        return max_size