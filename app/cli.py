from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Plant, Garden, Gardener, Base
from helpers  import (
    add_gardener,
    view_gardens,
    
)

# Create the engine
engine = create_engine('sqlite:///garden.db')

# Create all tables in the engine
Base.metadata.create_all(engine)

# Create a sessionmaker
Session = sessionmaker(bind=engine)

# Create a session
session = Session()

if __name__ == "__main__":
    print(
        """
,---.    ,---. _______   ,---.    ,---.          .-_'''-.      ____    .-------.     ______         .-''-.  ,---.   .--. 
|    \  /    |\  ____  \ |    \  /    |         '_( )_   \   .'  __ `. |  _ _   \   |    _ `''.   .'_ _   \ |    \  |  | 
|  ,  \/  ,  || |    \ | |  ,  \/  ,  |        |(_ o _)|  ' /   '  \  \| ( ' )  |   | _ | ) _  \ / ( ` )   '|  ,  \ |  | 
|  |\_   /|  || |____/ / |  |\_   /|  |        . (_,_)/___| |___|  /  ||(_ o _) /   |( ''_'  ) |. (_ o _)  ||  |\_ \|  | 
|  _( )_/ |  ||   _ _ '. |  _( )_/ |  |        |  |  .-----.   _.-`   || (_,_).' __ | . (_) `. ||  (_,_)___||  _( )_\  | 
| (_ o _) |  ||  ( ' )  \| (_ o _) |  |        '  \  '-   .'.'   _    ||  |\ \  |  ||(_    ._) ''  \   .---.| (_ o _)  | 
|  (_,_)  |  || (_{;}_) ||  (_,_)  |  |         \        / \ (_ o _) /|  |  \    / |       .'    \       / |  (_,_)\  | 
|  |      |  ||  (_,_)  /|  |      |  |          \  `-'`   | |  _( )_  ||  | \ `'   /|  (_.\.' /  \  `-'    /|  |    |  | 
'--'      '--'/_______.' '--'      '--'           `'-...-'   '.(_,_).' ''-'   `'-'  '-----'`       `'-..-'  '--'    '--' 
                                                                                                                        
        """
    )
    print("Hello, gardener! Welcome to the MBM Garden CLI.")
    plants = session.query(Plant).all()
    gardeners = session.query(Gardener).all()
    gardens = session.query(Garden).all()

    gardener_name = input("Name: ")
    name_check = False
    for gardener in gardeners:
        if gardener.name.lower() == gardener_name.lower():
            print(f"Welcome back, {gardener.name}.")
            name_check = True
    if not name_check:
        add_gardener(session, gardener_name)

    print("Here is a list of our current gardens:")
    view_gardens(gardens, plants, gardeners)

    # Close the session
    session.close()
