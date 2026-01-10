from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route("/run")
def run():
    # Replace this with your actual logic
    result = sum(range(10))
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)