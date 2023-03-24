from collections import defaultdict

class UnionFind:
    def __init__(self):
        self.parent = {}
        # self.weight = defaultdict(lambda:0)
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
                self.parent[a_parent] = b_parent
                # if self.weight[a_parent] > self.weight[b_parent]:
                #     self.parent[b_parent] = a_parent
                #     self.weight[a_parent] += 1
                # else :
                #     self.parent[a_parent] = b_parent
                #     self.weight[b_parent] += 1

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        uf = UnionFind()
        groups = defaultdict(list)
        for parent, child in pairs:
            uf.union(parent, child)
        for i in range (len(s)):
            groups[uf.find(i)].append(s[i])
        for key in groups.keys():
            groups[key].sort(reverse=True)
        result = []
        for i in range(len(s)): #get from 0(a), providing smallest result
            result.append(groups[uf.find(i)].pop())
        return "".join(result)
