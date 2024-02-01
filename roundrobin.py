import random

class RoundRobinLoadBalancer:
    """Implements the round robin load balancing algorithm"""

    def __init__(self, servers):
        self.servers = servers
        self.index = 0

    def get_server(self):
        """Returns the next server in the rotation"""
        server = self.servers[self.index]
        self.index = (self.index + 1) % len(self.servers)
        return server

servers = ["Server1", "Server2", "Server3"]
lb = RoundRobinLoadBalancer(servers)

active_connections = []

for i in range(100):
    if random.randint(0, 1) == 0 or not active_connections:
        # Make a new request
        selected_server = lb.get_server()
        active_connections.append(selected_server)
        print(f"Request {i+1}: New request came in. Servers available: {len(servers)}. Allocated to: {selected_server}")
    else:
        # Release a connection
        selected_server = random.choice(active_connections)
        active_connections.remove(selected_server)
        print(f"Request {i+1}: Connection released. Servers available: {len(servers)}. Released from: {selected_server}")
