from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import declarative_base


# Create the engine
engine = create_engine('sqlite:///garden.db')

# Create a session maker
Session = sessionmaker(bind=engine)

# Create a declarative base instance
Base = declarative_base()

# Define your models: Plant, Gardener, Garden
class Plant(Base):
    __tablename__ = 'plants'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    species = Column(String)
    season = Column(String)
    harvest_time = Column(Integer)
    quantity = Column(Integer)

class Gardener(Base):
    __tablename__ = 'gardeners'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)
    experience = Column(Integer)

class Garden(Base):
    __tablename__ = 'gardens'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)
    experience_req = Column(Integer)
    plant_id = Column(Integer, ForeignKey('plants.id'))
    gardener_id = Column(Integer, ForeignKey('gardeners.id'))

    plant = relationship('Plant', backref='garden')
    gardener = relationship('Gardener', backref='garden')

if __name__ == '__main__':
    # Create all tables defined in the models
    Base.metadata.create_all(engine)

    # Create a session
    session = Session()

    # Data Seeding - Create instances of plants, gardeners, gardens, and add them to the session
    plants = [
        Plant(
            name="Tomatoes",
            species="Solanum lycopersicum",
            season="Spring",
            harvest_time=10,
            quantity=12
        ),
        Plant (
            name="Kales",
            species="Phaseolus vulgaris",
            season="Summer",
            harvest_time=6,
            quantity=14
        ),
        # Add more Plant instances as needed
    ]

    gardeners = [
        Gardener(
            name="Jerrad Omondi",
            location="Homabay Kisumu",
            experience=3
        ),
        Gardener (
            name="Lewis Kipchirchir",
            location="Kericho Eldoret",
            experience=2
        ),
        # Add more Gardener instances as needed
    ]

    gardens = [
        Garden(
            name="Lavender Springs",
            location="Homabay,Kisumu",
            experience_req=3,
            plant_id=1,
            gardener_id=1
        ),
        Garden (
            name="Breezy Meadows",
            location="Kericho, Eldoret",
            experience_req=2,
            plant_id=2,
            gardener_id=2
        ),
        # Add more Garden instances as needed
    ]
    
    # Add all instances to the session
    session.add_all(plants)
    session.add_all(gardeners)
    session.add_all(gardens)

    # Commit the changes to the database
    session.commit()
