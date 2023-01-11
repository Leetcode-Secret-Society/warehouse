class Server:
    def __init__(self, id):
        self.id = id
        self.connected_servers = []
        self.distance_to_master = -1
    def add_connection(self, server):
        self.connected_servers.append(server)
class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        server_dict = dict()
        for edge in edges:
            u = edge[0]
            v = edge[1]
            if u not in server_dict:
                server_dict[u] = Server(u)
            if v not in server_dict:
                server_dict[v] = Server(v)
            server_dict[u].add_connection(server_dict[v])
            server_dict[v].add_connection(server_dict[u])
        queue = [server_dict[0]]
        current_distance = 0
        while queue:
            new_queue = []
            for server in queue:
                server.distance_to_master = current_distance
            while queue:
                server = queue.pop()
                for next_server in server.connected_servers:
                    if next_server.distance_to_master==-1:
                        new_queue.append(next_server)
            current_distance+=1
            queue = new_queue
        max_busy_time = 0
        for server_id, patience_time in enumerate(patience[1:]):
            distance = server_dict[server_id+1].distance_to_master
            mail_delivery_time_cost = distance*2
            retried_mails = mail_delivery_time_cost // patience_time
            if mail_delivery_time_cost % patience_time == 0:
                retried_mails -= 1
            if retried_mails == 0:
                busy_time = mail_delivery_time_cost
            else:
                busy_time = mail_delivery_time_cost + retried_mails*patience_time
            max_busy_time = max(max_busy_time, busy_time)

        return max_busy_time + 1



