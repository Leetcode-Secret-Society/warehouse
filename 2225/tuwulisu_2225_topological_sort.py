class Node:
    def __init__(self, id):
        self.id = id
        self.win_nodes = set()
        self.lose_nodes = set()
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        node_dict = {}
        for winner, loser in matches:
            if winner not in node_dict:
                node_dict[winner] = Node(winner)
            node_dict[winner].win_nodes.add(loser)
            if loser not in node_dict:
                node_dict[loser] = Node(loser)
            node_dict[loser].lose_nodes.add(winner)
        
        answer_0 = []
        answer_1 = [] 
        for i, node in node_dict.items():
            if len(node.lose_nodes) == 0:
                answer_0.append(i)
            if len(node.lose_nodes) == 1:
                answer_1.append(i)
        answer_0.sort()
        answer_1.sort()
        return [answer_0, answer_1]
