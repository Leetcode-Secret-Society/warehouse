class Trie_Node:
    def __init__(self):
        self.amount = 0
        self.next_nodes_dict = defaultdict(Trie_Node)
        self.added_key_value = dict()

class MapSum:

    def __init__(self):
        self.root = Trie_Node()
        

    def insert(self, key: str, val: int) -> None:
        curr_node = self.root
        for c in key:
            curr_node = curr_node.next_nodes_dict[c]
            if key not in curr_node.added_key_value:
                curr_node.amount += val
            else:
                curr_node.amount += val - curr_node.added_key_value[key]
            curr_node.added_key_value[key] = val
        

    def sum(self, prefix: str) -> int:
        curr_node = self.root
        for c in prefix:
            if c in curr_node.next_nodes_dict:
                curr_node = curr_node.next_nodes_dict[c]
            else:
                return 0
        return curr_node.amount
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
