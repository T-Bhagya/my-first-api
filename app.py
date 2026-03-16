from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "My first API is running!"})

@app.route("/users")
def users():
    data = [
        {"id": 1, "name": "Thilini"},
        {"id": 2, "name": "Kamal"}
    ]
    return jsonify(data)

if __name__ == "__main__":
    app.run()