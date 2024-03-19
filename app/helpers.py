from models import db, Plant, Garden, Gardener

def existing_selection( gardener_name, gardens, plants, gardeners): #gardener_name missing as first positonal
      exit_loop = False
      while exit_loop == False:
                choice = input("What would you like to do: \n-Type 'all' to see all gardens \n-Type 'plants' to see your available plants \n-Type 'create' to create a garden! \n-Type 'exit' to end session  \n")
                print(' ')
                if choice.lower() == "all":
                     view_gardens(gardens, plants, gardeners)
                elif choice.lower() == "plants":
                     view_plants(plants)
                elif choice.lower() == "create":
                     add_garden(gardener_name, plants, gardeners) #write a method to create a garden
                elif choice.lower() == "exit":
                    exit_loop = True #write an exit
                else:
                    error_message()


def add_gardener(gardener_name, gardens, plants, gardeners):
    print("Please join to view our list of gardens and plants available to you.  ")
    location_input = input("City, State: ")
    exp_input = input("Years of experience: ")

    new_gardener = Gardener(
        name = gardener_name,
        location = location_input,
        experience = exp_input
    )

    db.session.add(new_gardener)
    db.session.commit()
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

    selected_id = input("What garden would you like to visit? Please select the corresponding ID: ")
    YES = ['y','ye','yes']
    NO = ['n', 'no']
    for garden in gardens:
        if str(garden.id) == selected_id:
             print(f"Welcome to {garden.name}, a {garden.plant.name} garden, located in {garden.location}. ")
             wtp = input(f"Would you like to plant some {garden.plant.name}? Y/N: ")
             if wtp.lower() in YES:
                  print("Yes statement")
                  pass #put in Bryants method
             elif wtp.lower() in NO:
                  print("No statement")
                  pass
             else:
                  error_message()

                  
            #  if isinstance(wtp, int) and 0<int

def view_plants(plants):
    print("-" * 100)
    print(
        f'| {"ID":<0} | {"Name":<15} | {"Species":<20} | {"Season":<10} | {"Harvest Time":<21} | {"Quantity":<10} |'
    )
    print("-" * 100)
    for plant in plants:
        id_spaces = 3- len(str(plant.id))
        name_spaces = 15 - len(plant.name)
        species_spaces = 20 - len(plant.species)
        season_spaces = 10 - len(plant.season)
        harvest_spaces = 15 - len(str(plant.harvest_time))
        quantity_spaces = 10 - len(str(plant.quantity))
        
        print(
            f'|{" "}{plant.id}{" " * id_spaces}| {plant.name}{" " * name_spaces} | {plant.species}{" " * species_spaces} | {plant.season}{" " * season_spaces} | {plant.harvest_time} weeks{" " * harvest_spaces} | {plant.quantity}{" " * quantity_spaces} |'
        )
    print("-" * 100)

    # id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String)
    # species = db.Column(db.String)
    # season = db.Column(db.String)
    # harvest_time = db.Column(db.Integer)
    # #harvest_time is in weeks
    # quantity = db.Column(db.Integer)



def add_garden(gardener_name, plants, gardeners):
    garden_input = input("What would you like to call your garden? ")
    location_input = input("City, State: ")

    g_id= None
    p_id = None
    garden_exp = None
    
    print(f"Here's a list of the plants currently available to be planted: ")
    view_plants(plants)

    print("From the above, select a plant, or introduce a new plant: ") 
    #Bryants new plant creation needed
    plant_input = input("What would you like to plant? Please select the corresponding plant ID: \nType 'new' to plant a new plant: \n") 
    if plant_input == "new":
         pass #need Bryants new plant when typing new
    elif plant_input:
        for plant in plants:
            if str(plant.id) == plant_input:
                plant_loop = False
                while plant_loop == False:
                    p_id = plant.id
                    quantity_to_plant = input(f"How many {plant.name} would you like to plant? ")
                    quantity_to_plant = int(quantity_to_plant)
                    if isinstance(quantity_to_plant, int) and 0 < quantity_to_plant <= 10:
                        plant.quantity += quantity_to_plant
                        print(f"Succesfully planted {quantity_to_plant} {plant.name}." )
                        plant_loop = True
                        print(plant_loop)
                        # break
                    elif quantity_to_plant > 10:
                        print(f"Not enough time to plant that many {plant.name}. Try a smaller amount. ") 
                    else:
                        error_message()
                     
    else:
         error_message()
    

    
    for gardener in gardeners:
        if gardener.name == gardener_name:
            g_id = gardener.id
            garden_exp = gardener.experience
    


    new_garden = Garden(
        name = garden_input,
        location = location_input,
        experience_req = garden_exp,
        gardener_id = g_id,
        plant_id = p_id
    )

    db.session.add(new_garden)
    db.session.commit()
    print(f"Congratulations! You've successfully created a community garden, would you like to go to {new_garden.name}? Type Y to continue to your garden and plant, or m to go back to the main menu.")

    #an input to bring you back to the main menu, something to take you to the created garden. A success message

def error_message():
        print("The input you've made is invalid, please try again.")

def visit_garden(gardens):
     pass
     


    #create takes to helper that is associated to their garden ID and then in there they can plant a new plant
    #or plant a plant that's already in our plant list, exp req = plant
    #visiting, how many bush beans would you like to plant = type number NO isinstance(variable_plant, int) and variable is 0<variable_plant<10 = error
    #if NUMBER > 10 you do not have time to plant that many plants

    #VISIT, make a garden, 