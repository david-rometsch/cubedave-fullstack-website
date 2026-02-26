from flask_sqlalchemy import SQLAlchemy
from db import db

class Cube (db.Model):
    id =  db.Column(db.Integer, primary_key=True)
      q

     q q q q
    img = db.Column(db.String(100), nullable=False)     # will be an existing file path later!

    '''@classmethod
    def create(cls, name, image):
        return cls(name, image)'''

    def __repr__(self): 
        return f"id: {id}, name: {name}, image-name: {img}"
