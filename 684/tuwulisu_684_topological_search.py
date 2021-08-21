class Node:
    def __init__(self, n):
        self.n = n
        self.connected_nodes = []
    def add_adj_node(self, adj_node):
        self.connected_nodes.append(adj_node)
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        node_dict = dict()
        node_set = set()
        for edge in edges:
            lnode = edge[0]
            rnode = edge[1]
            if lnode not in node_dict:
                node_dict[lnode]=Node(lnode)
            if rnode not in node_dict:
                node_dict[rnode]=Node(rnode)
            node_dict[lnode].add_adj_node(node_dict[rnode])
            node_dict[rnode].add_adj_node(node_dict[lnode])
            node_set.add(lnode)
            node_set.add(rnode)
        queue=[]
        for node_id in node_set:
            if len(node_dict[node_id].connected_nodes)==1:
                queue.append(node_dict[node_id])
        while queue:
            new_queue=[]
            for node in queue:
                for adj_node in node.connected_nodes:
                    adj_node.connected_nodes.remove(node)
                node_set.remove(node.n)
            for node_id in node_set:
                if len(node_dict[node_id].connected_nodes)==1:
                    new_queue.append(node_dict[node_id])
            queue=new_queue
        for edge in reversed(edges):
            lnode = edge[0]
            rnode = edge[1]
            if lnode in node_set and rnode in node_set:
                return [lnode,rnode]
                
        
