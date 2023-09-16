#!/usr/bin/python3
from flask import Flask, request, jsonify
from db import db, People

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///people.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.route('/api', methods=['POST'])
def create_person():
    data = request.json
    if 'name' in data:
        name = data['name']
        new_person = Person(name=name)
        db.session.add(new_person)
        db.session.commit()
        return jsonify({
            "id": new_person.id,
            "name": new_person.name
        }), 201
    else:
        return jsonify({"message": "Name is required in the request data"}), 400


@app.route("/api/<int:id>", methods=["GET", "PUT", "DELETE"])
def manage_person(id):
    person = People.query.get_or_404(id)

    if request.method == "GET":
        return jsonify(
            {
                "id": person.id,
                "name": person.name,
                "age": person.age,
                "email": person.email,
            }
        )
    elif request.method == "PUT":
        data = request.json
        person.name = data.get("name", person.name)
        person.age = data.get("age", person.age)
        person.email = data.get("email", person.email)
        db.session.add(person)
        db.session.commit()
        return jsonify({"message": "Person updated successufully"}), 201

    elif request.method == "DELETE":
        db.session.delete(person)
        db.session.commit()
        return jsonify({"message": "Person deleted successufully"}), 201


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run()
