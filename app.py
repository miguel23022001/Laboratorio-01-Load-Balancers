from flask import Flask, jsonify
import argparse

app = Flask(__name__)

@app.route('/hello')
def hello():
    return jsonify({"message": "Success"})

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run the Flask app')
    parser.add_argument('--port', type=int, default=5000, help='Port for the app')

    args = parser.parse_args()
    app.run(port=args.port)
