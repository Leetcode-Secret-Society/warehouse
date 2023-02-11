import collections
class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        print(f"{len(sentence1)=}, {len(sentence2)=}")
        if len(sentence1) != len(sentence2):
            return False
        parent = collections.defaultdict()
        
        def find(x):
            if x not in parent:
                parent[x] = x
            while x != parent[x]:
                x = parent[x]
            return x   
        
        def union(l, r):
            l_parent = find(l)        
            r_parent = find(r)
            if l_parent != r_parent:
                parent[l_parent] = r_parent
                
        for i, j in similarPairs:
            union(i, j)
        
        for i in range(len(sentence1)):
            if not find(sentence1[i]) == find(sentence2[i]):
                return False
        return True
