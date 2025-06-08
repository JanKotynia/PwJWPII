from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    priority = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "priority": self.priority
        }

with app.app_context():
    db.create_all()

@app.route("/tasks", methods=["GET"])
def getlist():
    tasks = Task.query.all()
    result = [task.to_dict() for task in tasks]
    return jsonify(result)

@app.route("/create", methods=["POST"])
def createtask():
    data=request.get_json()
    if not data or not all(k in data for k in ("name", "priority")):
        return jsonify({"error": "Missing data"}), 400

    new_task = Task(name=data["name"], priority=data["priority"])
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"message": "Task dodany!"}), 201

@app.route("/delete/<int:id>", methods=["DELETE"])
def deletelasttask(id):
    task = db.session.get(Task, id)
    if task:
        db.session.delete(task)
        db.session.commit()
        return jsonify({"message": f"Teacher {id} deleted"})
    return jsonify({"error": "Missing data"}), 400

# @app.route("/update/<key>", methods=["PATCH"])
# def updateTask(key):
#     if key in tasks:
#         zadanie = request.json.get("zadanie")
#         tasks[key] = zadanie
#         return jsonify({"updated": {key: zadanie}}), 200
#     else:
#         return jsonify({"error": "Nie znaleziono zadania"}), 400

if __name__ == "__main__":
    app.run(debug=True)