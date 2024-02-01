import random

class WeightedRoundRobinLoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.index = 0
        self.current_weight = 0
        self.max_weight = max(server['weight'] for server in servers)

    def get_server(self):
        while True:
            self.index = (self.index + 1) % len(self.servers)
            if self.index == 0:
                self.current_weight = self.current_weight - 1
                if self.current_weight <= 0:
                    self.current_weight = self.max_weight
            if self.servers[self.index]['weight'] >= self.current_weight:
                return self.servers[self.index]['name']

servers = [{"name": "Server1", "weight": 1}, {"name": "Server2", "weight": 2}, {"name": "Server3", "weight": 3}]
lb = WeightedRoundRobinLoadBalancer(servers)

active_connections = {}

for i in range(100):
    if random.randint(0, 1) == 0 or not active_connections:
        # Make a new request
        selected_server = lb.get_server()
        active_connections[i] = selected_server
        print(f"Request {i+1}: New request came in. Servers available: {len(servers)}. Allocated to: {selected_server}")
    else:
        # Release a connection
        request_id, selected_server = random.choice(list(active_connections.items()))
        del active_connections[request_id]
        print(f"Request {i+1}: Connection from request {request_id+1} released. Servers available: {len(servers)}. Released from: {selected_server}")
