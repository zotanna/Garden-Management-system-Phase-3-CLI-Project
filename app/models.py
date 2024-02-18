from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Plant(db.Model):
    __tablename__ =  "plants"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)
    season = db.Column(db.String)
    harvest_time = db.Column(db.Integer)
    #harvest_time is in weeks

    def __repr__(self):
        return f"<Plant {self.name}"
    
class Gardener(db.Model):
    __tablename__ =  "gardeners"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    location = db.Column(db.String)
    experience = db.Column(db.Integer)

    def __repr__(self):
        return f"<Gardener {self.name}"

class Garden(db.Model):
    __tablename__ = "gardens"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    location = db.Column(db.String)
    experience_req = db.Column(db.Integer)

    plant_id = db.Column(db.Integer)
    gardener_id = db.Column(db.Integer)

    def __repr__(self):
        return f"<Garden {self.name}"