from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey

from sqlalchemy.ext.declarative import declarative_base

# Create engine
engine = create_engine('sqlite:///', echo=True)

# Create a session class
Session = sessionmaker(bind=engine)

# Create a base class for declarative class definitions
Base = declarative_base()

# Define models
class Plant(Base):
    __tablename__ = "plants"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    species = Column(String)
    season = Column(String)
    harvest_time = Column(Integer)

    def __repr__(self):
        return f"<Plant {self.name}>"

class Gardener(Base):
    __tablename__ = "gardeners"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)
    experience = Column(Integer)

    def __repr__(self):
        return f"<Gardener {self.name}>"

class Garden(Base):
    __tablename__ = "gardens"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)
    experience_req = Column(Integer)

    plant_id = Column(Integer, ForeignKey('plants.id'))
    gardener_id = Column(Integer, ForeignKey('gardeners.id'))

    def __repr__(self):
        return f"<Garden {self.name}>"

# Create tables
Base.metadata.create_all(engine)

