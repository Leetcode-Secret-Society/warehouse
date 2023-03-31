
from collections import defaultdict

class UnionFind:
    def __init__(self):
        self.parent = {}
        self.weight = defaultdict(lambda:0)
    def find(self,pos):
        if pos in self.parent:
            if self.parent[pos] != pos:
                self.parent[pos] = self.find(self.parent[pos])
        else:
            self.parent[pos] = pos
        return self.parent[pos]
    def union(self,a,b):
            a_parent, b_parent = self.find(a), self.find(b)
            if a_parent != b_parent: 
                # self.parent[a_parent] = b_parent
                if self.weight[a_parent] > self.weight[b_parent]:
                    self.parent[b_parent] = a_parent
                    self.weight[a_parent] += 1
                else :
                    self.parent[a_parent] = b_parent
                    self.weight[b_parent] += 1

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        uf = UnionFind()
        for parent, child in allowedSwaps: 
            uf.union(parent, child)
        
        # key is the component, value is the set of indices in same component
        groups = defaultdict(set)  
        for i in range(len(source)):
            groups[uf.find(i)].add(i)

        ans = 0
        for indices in groups.values():
            source_count = Counter([source[i] for i in indices])
            target_count = Counter([target[i] for i in indices])
            diff_count = source_count - target_count
            ans += sum(diff_count.values())

        return ans
