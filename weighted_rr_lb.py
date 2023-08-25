from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

servers = [
    {"ip": "http://127.0.0.1:5000", "weight": 7},
    {"ip": "http://127.0.0.1:5001", "weight": 5},
    {"ip": "http://127.0.0.1:5002", "weight": 3}
]

current_server = 0
remaining_weight = 0

@app.route('/')
def balance_request():
    global current_server, remaining_weight

    if remaining_weight <= 0:
        current_server = (current_server + 1) % len(servers)
        remaining_weight = servers[current_server]["weight"]

    server_ip = servers[current_server]["ip"]
    remaining_weight -= 1
    print(f"SERVIDOR: {server_ip}/hello")
    response = requests.get(f"{server_ip}/hello")
    return response.json()

if __name__ == "__main__":
    app.run(port=8000)
