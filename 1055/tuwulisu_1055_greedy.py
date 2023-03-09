class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        source_set = set(source)
        nearest_map = defaultdict(int)
        nearest_map_at_pos = [copy.copy(nearest_map)]
        for i, c in enumerate(reversed(source)):
            nearest_map[c]=len(source)-i-1
            nearest_map_at_pos.append(copy.copy(nearest_map))
        nearest_map_at_pos.reverse()
        current_pos_in_source = 0
        count_of_subseq = 0
        #print(nearest_map_at_pos)
        for c in target:
            if c not in source_set:
                return -1
            if c not in nearest_map_at_pos[current_pos_in_source]:
                count_of_subseq+=1
                current_pos_in_source=0
            current_pos_in_source = nearest_map_at_pos[current_pos_in_source][c]+1
                
        return count_of_subseq+1
