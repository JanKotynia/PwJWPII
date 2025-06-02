from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

tasks = {
    "1": "zrobic herbate",
    "2": "zrobic ciasto"
}

@app.route("/tasks", methods=["GET"])
def getlist():
    return jsonify([
        {"time": key, "name": value}
        for key, value in tasks.items()
    ])

@app.route("/about", methods=["GET"])
def about():
    return jsonify([
        {"time": key, "name": value}
        for key, value in tasks.items()
    ])

@app.route("/create", methods=["POST"])
def createtask():
    czas = request.json.get("time")
    zadanie = request.json.get("name")

    if not czas or not zadanie:
        return jsonify({"message": "You must include czas i zadanie"}), 400

    tasks[czas] = zadanie
    return jsonify({"message": "Task dodany!"}), 201

@app.route("/delete", methods=["DELETE"])
def deletelasttask():
    if tasks:
        deleted_key, deleted_value = tasks.popitem()
        return jsonify({"deleted": {deleted_key: deleted_value}}), 200
    else:
        return jsonify({"error": "Lista jest pusta"}), 400

@app.route("/delete/<key>", methods=["DELETE"])
def deletekeytask(key):
    if key in tasks:
        deleted_value = tasks.pop(key)
        return jsonify({"deleted": {key: deleted_value}}), 200
    else:
        return jsonify({"error": "Nie znaleziono zadania"}), 400

@app.route("/update/<key>", methods=["PATCH"])
def updateTask(key):
    if key in tasks:
        zadanie = request.json.get("zadanie")
        tasks[key] = zadanie
        return jsonify({"updated": {key: zadanie}}), 200
    else:
        return jsonify({"error": "Nie znaleziono zadania"}), 400

if __name__ == "__main__":
    app.run(debug=True)