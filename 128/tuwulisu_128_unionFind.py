class Solution:
    def find(self, node):
        if node[0]!=node[3]:
            group_node = self.find(self.nodes[node[0]])
            node[0] = group_node[0]
            return group_node
        else:
            return node
    
    def merge(self, node1, node2):
        node1 = self.find(node1)
        node2 = self.find(node2)
        if node1 is node2:
            return
        rank1 = node1[1]
        rank2 = node2[1]
        if rank1 < rank2:
            node1, node2 = node2, node1
            rank1, rank2 = rank2, rank1
        node2[0] = node1[0]
        node1[2] += node2[2]
        if rank1 == rank2:
            node1[1] += 1
            node2[1] += 1
        else:
            node2[1] = node1[1]
            
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        new_nums = []
        set_ = set()
        for n in nums:
            if n not in set_:
                new_nums.append(n)
            set_.add(n)
        nums = new_nums
        dict_ = {n:i for i, n in enumerate(nums)}
        self.nodes = [[i, 0, 1, i] for i in range(len(nums))]
        
        for i, n in enumerate(nums):
            #print(i,n)
            if n-1 in dict_:
                self.merge(self.nodes[dict_[n-1]], self.nodes[i])
            if n+1 in dict_:
                self.merge(self.nodes[dict_[n+1]], self.nodes[i])
                
            #print(self.nodes)
        return max([node[2] for node in self.nodes if node[0]==node[3]])
            
