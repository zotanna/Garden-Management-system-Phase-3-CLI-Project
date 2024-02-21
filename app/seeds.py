from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Plant, Gardener, Garden, Base

# Create the engine
engine = create_engine('sqlite:///garden.db')

# Create a session class
Session = sessionmaker(bind=engine)

# Create a session
session = Session()

# Clear out existing data
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Create instances of models
plants = [
    Plant(name="Tomatoes", species="Solanum lycopersicum", season="Spring", harvest_time=10, quantity=12),
    Plant(name="Bush Beans", species="Phaseolus vulgaris", season="Summer", harvest_time=6, quantity=14),
    Plant(name="Watermelons", species="Citrullus lanatus", season="Summer", harvest_time=11, quantity=15),
    Plant(name="Pumpkins", species="Cucurbita pepo", season="Fall", harvest_time=15, quantity=10),
    Plant(name="Strawberries", species="Fragaria ananassa", season="Spring", harvest_time=5, quantity=6)
]

gardeners = [
    Gardener(name="Emily Johnson", location="Seattle, WA", experience=3),
    Gardener(name="Michael Thompson", location="Austin, TX", experience=2),
    Gardener(name="Luisa Rodriguez", location="Chicago, IL", experience=1),
    Gardener(name="Sophie Clark", location="San Francisco, CA", experience=4),
    Gardener(name="Juan Hernandez", location="Miami, FL", experience=0)
]

gardens = [
    Garden(name="Sunshine Paradise", location="Seattle, WA", experience_req=3, plant_id=1, gardener_id=1),
    Garden(name="Breezy Meadows", location="Austin, TX", experience_req=2, plant_id=2, gardener_id=2),
    Garden(name="City Retreat", location="Chicago, IL", experience_req=1, plant_id=3, gardener_id=3),
    Garden(name="Serene Haven", location="San Francisco, CA", experience_req=4, plant_id=4, gardener_id=4),
    Garden(name="Tropical Oasis", location="Miami, FL", experience_req=0, plant_id=5, gardener_id=5)
]

# Add instances to the session
session.add_all(plants)
session.add_all(gardeners)
session.add_all(gardens)

# Commit the session to the database
session.commit()

# Close the session
session.close()

