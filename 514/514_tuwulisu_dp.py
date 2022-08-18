class Node:
    def __init__(self, char: str, index: int):
        self.char = char
        self.id = f"{char}{index}"
        self.shortest_path_length = 0
class Solution:
    def cal_distance(self, i, j, l):
        d = abs(i-j)
        if d>l/2:
            d = l/2 - (d - (l/2))
        return int(d)
    
    def findRotateSteps(self, ring: str, key: str) -> int:
        node_list = []
        char_nodes_dict: Dict[str, List[Node]] = {}
        distance_dict = {}
        for c in ring:
            if c not in char_nodes_dict:
                index=0
                node = Node(c, index)
                char_nodes_dict[c] = [node]
            else:
                index=len(char_nodes_dict[c])
                node = Node(c, index)
                char_nodes_dict[c].append(node)
            node_list.append(node)
        for i in range(len(node_list)):
            for j in range(i, len(node_list)):
                nodei = node_list[i]
                nodej = node_list[j]
                distance = self.cal_distance(i, j, len(node_list))
                distance_dict[(nodei, nodej)] = distance
                distance_dict[(nodej, nodei)] = distance
        previous_nodes = [char_nodes_dict[ring[0]][0]]
        for c in key:
            for target_node in char_nodes_dict[c]:
                path_length_list = [previous_node.shortest_path_length + distance_dict[(previous_node, target_node)]  for previous_node in previous_nodes] 
                target_node.shortest_path_length = min(path_length_list)

            previous_nodes = char_nodes_dict[c]
        length_list = [node.shortest_path_length for node in previous_nodes]
        #print(char_nodes_dict)
        #print(length_list)
        return min(length_list)+len(key)
