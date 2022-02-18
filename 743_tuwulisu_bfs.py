import heapq
class Node:
    def __init__(self, id):
        self.id = id
        self.out_directions = []
        self.received_time = float('inf')
        self.visited = False

class Solution:
    def get_node(self, id):
        return self.node_list[id-1]
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        self.node_list = [Node(i+1) for i in range(n)]
        for direction in times:
            from_node_id = direction[0]
            to_node_id = direction[1]
            cost = direction[2]
            self.get_node(from_node_id).out_directions.append((self.get_node(to_node_id), cost))
        self.get_node(k).visited = True
        self.get_node(k).received_time = 0
        node_queue = [self.get_node(k)]
        while node_queue:
            next_queue = []
            for node in node_queue:
                node.visited = True
                for out_node, cost in node.out_directions:
                    if node.received_time + cost < out_node.received_time:
                        out_node.received_time = node.received_time + cost
                        next_queue.append(out_node)
            node_queue = next_queue
        max_time = 0
        for node in self.node_list:
            if node.visited:
                max_time = max(max_time, node.received_time)
            else:
                break
        else:
            return max_time
        return -1
                
            
        
                
        
                
