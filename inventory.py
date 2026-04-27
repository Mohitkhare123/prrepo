from flask import Flask, jsonify, request

app = Flask(__name__)

inventory = []

@app.route("/")
def home():
    return "Hello, my name is Mohit Khare. I have built Inventory Management Service Application."

@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(inventory)

@app.route("/items", methods=["POST"])
def add_item():
    data = request.json
    inventory.append(data)
    return {"message": "Item added successfully"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)