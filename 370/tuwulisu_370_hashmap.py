from collections import defaultdict
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        hash_map = defaultdict(int)
        for i, j, c in updates:
            hash_map[i]+=c
            hash_map[j+1]-=c
        num = 0
        ans = []
        for i in range(length):
            num+=hash_map[i]
            ans.append(num)
        return ans
            
