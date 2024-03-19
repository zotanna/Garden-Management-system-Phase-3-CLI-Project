from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Plant(db.Model):
    __tablename__ =  "plants"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)
    season = db.Column(db.String)
    harvest_time = db.Column(db.Integer)
    #harvest_time is in weeks
    quantity = db.Column(db.Integer)
    

    gardeners = db.relationship('Gardener', secondary="gardens", back_populates="plants")

    gardens = db.relationship(
        "Garden", back_populates="plant", overlaps="plants,gardeners"
    )

    def __repr__(self):
        return f"<Plant {self.name}"
    
class Gardener(db.Model):
    __tablename__ =  "gardeners"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    location = db.Column(db.String)
    experience = db.Column(db.Integer)

    plants = db.relationship('Plant', secondary="gardens", back_populates="gardeners")

    gardens = db.relationship(
        "Garden", back_populates="gardener", overlaps="plants,gardeners"
    )

    def __repr__(self):
        return f"<Gardener {self.name}"

class Garden(db.Model):
    __tablename__ = "gardens"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    location = db.Column(db.String)
    experience_req = db.Column(db.Integer)

    plant_id = db.Column(db.Integer, db.ForeignKey('plants.id'))
    gardener_id = db.Column(db.Integer, db.ForeignKey('gardeners.id'))

    plant = db.relationship(
        "Plant", back_populates="gardens", overlaps="plants,gardeners"
    )

    gardener = db.relationship(
        "Gardener", back_populates="gardens", overlaps="plants,gardeners"
    )

    def __repr__(self):
        return f"<Garden {self.name}"