from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
   # age = db.Column(db.Integer, nullable=False)
    #email = db.Column(db.String(75), nullable=False)
