from flask import Flask, request, jsonify
import random
import socket
import requests

app = Flask(__name__)

servers = [
    {"name": "Server A", "ip": "http://127.0.0.1:5000"},
    {"name": "Server B", "ip": "http://127.0.0.1:5001"},
    {"name": "Server C", "ip": "http://127.0.0.1:5002"}
]

class Client:
    def __init__(self):
        self.client_ids = [random.randint(1, 100000) for _ in range(10)]  # Simulated client IDs
        self.index = 0

    def get_next_id(self):
        client_id = self.client_ids[self.index]
        self.index = (self.index + 1) % len(self.client_ids)
        return client_id

client = Client()

def hash_function(data):
    return hash(data) % len(servers)

@app.route('/')
def balance_request():
    client_id = client.get_next_id()
    simulated_ip = f"{socket.inet_ntoa(client_id.to_bytes(4, 'big'))}"
    server_index = hash_function(simulated_ip)

    server = servers[server_index]
    server_ip = server["ip"]
    server_name = server["name"]

    response = requests.get(f"{server_ip}/hello")
    print(f"Request sent to {server_name} from client {simulated_ip}: {response.text}")
    return f"Request sent to {server_name} from client {simulated_ip}: {response.text}"

if __name__ == "__main__":
    app.run(port=8000)
