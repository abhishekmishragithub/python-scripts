

import random

class LeastConnectionsLoadBalancer:
    def __init__(self, servers):
        self.servers = {server: 0 for server in servers}

    def get_server(self):
        server = min(self.servers, key=self.servers.get)
        self.servers[server] += 1
        print(f"New request came in. Server {server} was selected. Current server loads: {self.servers}")
        return server

    def release_connection(self, server):
        if self.servers[server] > 0:
            self.servers[server] -= 1
            print(f"Connection released from Server {server}. Current server loads: {self.servers}")

servers = ["Server1", "Server2", "Server3"]
lb = LeastConnectionsLoadBalancer(servers)

active_connections = []

for _ in range(15):
    if random.randint(0, 1) == 0 or not active_connections:
        # Make a new request
        selected_server = lb.get_server()
        active_connections.append(selected_server)
        print(f"active connections: {active_connections}")
    else:
        # Release a connection
        selected_server = random.choice(active_connections)
        lb.release_connection(selected_server)
        active_connections.remove(selected_server)
