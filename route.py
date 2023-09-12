#!/usr/bin/python3
from flask import Flask
import db

app = Flask(__name__)


app.route('/api', methods=['POST'])


def create_person():
    data = request.json
    new_person = Person(**data)
    db.session.add(new_person)
    db.session.commit()
    return jsonify({'message': 'Person created successufully'}), 201


app.route('/api/<int:id>', methods=['GET', 'PUT', 'DELETE'])


def manage_person(id):
    person = Person.query.get_or_404(id)

    if request.method == 'GET':
        return jsonify({
            'id': person.id,
            'name': person.name,
            'age':  person.age,
            'email': person.email
        })
    elif request.method == 'PUT':
        data = request.json
        person.name = data.get('name', person.name)
        person.age = data.get('age', person.age)
        person.email = data.get('email', person.email)
        db.session.commit()

    elif request.method == 'DELETE':
        db.session.delete(person)
        db.session.commit()
        return jsonify({'message': 'Person deleted successfully'}), 204


if __name__ == '__main__':
    app.run(debug=True)
