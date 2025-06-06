from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///teachers.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    subject = db.Column(db.String, nullable=False)
    time = db.Column(db.Integer)
    
    def to_dict(self):
       return {
           "id": self.id,
           "name": self.name,
           "subject": self.subject,
           "time": self.time
       }
    
with app.app_context():
    db.create_all()

@app.route('/data', methods=['GET'])
def home():
    teachers = Teacher.query.all()
    result = [teacher.to_dict() for teacher in teachers]
    return jsonify(result)


@app.route('/data', methods=['POST'])
def add():
    data = request.get_json()
    if not data or not all(k in data for k in ("name", "subject", "time")):
        return jsonify({"error": "Missing data"}), 400

    new_teacher = Teacher(name=data["name"], subject=data["subject"], time=data["time"])
    db.session.add(new_teacher)
    db.session.commit()
    return jsonify(new_teacher.to_dict()), 201

@app.route('/teachers/<int:id>', methods=['DELETE'])
def delete_teacher(id):
    teacher = db.session.get(Teacher, id)
    if teacher:
        db.session.delete(teacher)
        db.session.commit()
        return jsonify({"message": f"Teacher {id} deleted"})
    return jsonify({"error": "Teacher not found"}), 404


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False) 