import random
import hashlib

class IPHashLoadBalancer:
    def __init__(self, servers):
        self.servers = servers

    def get_server(self, ip_address):
        hash_value = int(hashlib.sha256(ip_address.encode()).hexdigest(), 16)
        return self.servers[hash_value % len(self.servers)]

servers = ["Server1", "Server2", "Server3"]
lb = IPHashLoadBalancer(servers)

active_connections = {}

for i in range(100):
    if random.randint(0, 1) == 0 or not active_connections:
        # Make a new request
        ip = f"192.168.1.{random.randint(1, 100)}"
        selected_server = lb.get_server(ip)
        active_connections[ip] = selected_server
        print(f"Request {i+1}: New request from IP {ip} came in. Servers available: {len(servers)}. Allocated to: {selected_server}")
    else:
        # Release a connection
        ip, selected_server = random.choice(list(active_connections.items()))
        del active_connections[ip]
        print(f"Request {i+1}: Connection from IP {ip} released. Servers available: {len(servers)}. Released from: {selected_server}")
