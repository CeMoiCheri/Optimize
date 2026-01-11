from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/run")
def run():
    try:
        x = int(request.args.get("x", 0))
    except ValueError:
        x = 0

    result = sum(range(x))
    return jsonify({"result": result})

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
