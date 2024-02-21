from sqlalchemy import Column,Integer,String,ForeignKey,desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.associationproxy import association_proxy


# Create the engine

engine = create_engine('sqlite:///garden.db')  # Set echo to True to see the SQL statements

# Create a session class
Session = sessionmaker(bind=engine)

session=Session()

# Create a base class for declarative class definitions
Base = declarative_base()

# Define the models
class Plant(Base):
    __tablename__ = "plants"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    species = Column(String)
    season = Column(String)
    harvest_time = Column(Integer)
    quantity = Column(Integer)
    # harvest_time is in weeks

    gardens = relationship('Garden', backref='plants')

    def __repr__(self):
        return f"<Plant {self.name}>"


class Gardener(Base):
    __tablename__ = "gardeners"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)
    experience = Column(Integer)

    gardens = relationship('Garden', backref='gardeners')

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

# Example usage:
if __name__ == "__main__":
    session = Session()
    session.close()
    
    