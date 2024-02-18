from models import Plant, Gardener, Garden, Session

if __name__ == "__main__":
    # Create a session using context manager
    with Session() as session:
        # Create instances of models
        plant1 = Plant(name='Rose', species='Rosa', season='Spring', harvest_time=12)
        gardener1 = Gardener(name='John', location='New York', experience=5)
        garden1 = Garden(name='Rose Garden', location='New York', experience_req=3)

        # Add instances to the session
        session.add(plant1)
        session.add(gardener1)
        session.add(garden1)

        # Commit the session to the database
        session.commit()
