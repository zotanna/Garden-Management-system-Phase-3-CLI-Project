from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Plant, Garden, Gardener, Base

# Create the engine
engine = create_engine('sqlite:///garden.db')

# Create all tables in the engine
Base.metadata.create_all(engine)

# Create a sessionmaker
Session = sessionmaker(bind=engine)

# Create a session
session = Session()

def add_gardener(session, gardener_name):
    location_input = input("City, State: ")
    exp_input = int(input("Years of experience: "))

    # Check if the gardener already exists
    existing_gardener = session.query(Gardener).filter_by(name=gardener_name).first()
    if existing_gardener:
        print(f"{gardener_name} already exists in the database.")
        return

    new_gardener = Gardener(
        name=gardener_name,
        location=location_input,
        experience=exp_input
    )

    session.add(new_gardener)
    session.commit()
    print(f"Welcome to MBM Gardens, {gardener_name}. You've been added to our list of gardeners.")

def view_gardens(gardens, plants, gardeners):
    print("-" * 112)
    print(
        f'| {"ID":<3} | {"Name":<20} | {"Location":<20} | {"XP LVL":<10} | {"Plant":<20} | {"Gardener":<20} |'
    )
    print("-" * 112)
    for garden in gardens:
        id_spaces = 3 - len(str(garden.id))
        name_spaces = 20 - len(garden.name)
        location_spaces = 20 - len(garden.location)
        experience_spaces = 10 - len(str(garden.experience_req))
        plant_name = garden.plant.name
        plant_spaces = 20 - len(plant_name)
        gardener_name = garden.gardener.name
        gardener_spaces = 20 - len(gardener_name)
        print(
            f'| {garden.id}{" " * id_spaces} | {garden.name}{" " * name_spaces} | {garden.location}{" " * location_spaces} | {garden.experience_req}{" " * experience_spaces} | {plant_name}{" " * plant_spaces} | {gardener_name}{" " * gardener_spaces} |'
        )
    print("-" * 112)

# Example usage
if __name__ == '__main__':
    # Test adding a gardener
    add_gardener(session, "John Doe")

    # Test viewing gardens (assuming you have gardens loaded from somewhere)
    gardens = session.query(Garden).all()
    plants = session.query(Plant).all()
    gardeners = session.query(Gardener).all()
    view_gardens(gardens, plants, gardeners)  # Pass the necessary arguments

    # Close the session
    session.close()