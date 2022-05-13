import random


# Initial values.
destinations = ['San Miguel De Allende', 'Udaipur', 'Istanbul', 'Tokyo', 'Florence', 'Bangkok', 'Rome', 'Jaipur', 'Cape Town',
                'Luang Prabang']
lists_restaurants = [['La Doña de San Miguel', 'Rustica', 'Hecho en Mexico', 'The Restaurant',
                    'Lavanda Cafe', 'Restaurante 1826', 'Trazo 1810', 'Marsala', 'El Rinconcito','Carajillo San Miguel'],
                    ['Raaj Bagh', 'Restaurant Harigarh', 'Aravali Lakview', 'Syah', 'Skyfall Rooftop Restaurant', 
                    'SABOR World Cuisine', 'Jaajam Restaurant', 'Kotra Haveli Roof Top Restaurant & Cafe', 
                    'Jaiwana Haveli Roof Top', 'Helloboho Lake Side Restaurant'],
                    ['Pepo Restaurant', 'Kosk 1981 Cafe & Resaurant', 'Isanbul Kebab Cafe & Restaurant', 
                    'Three Partners Cafe & Restaurant', 'Garden 1897 Restaurant', 'Isanbul Anatolion Cuisine', 
                    'Mivan Restauran Cafe', 'Resto Han','Last Ottoman Cafe & Restaurant', 'Sultan Palace Cafe Restaurant'],
                    ['Gyopao Gyoza Roppongi', 'Star Star', 'Ninja Cafe & Bar Asakusa', 'Mugi no Oto', 
                    'Ginza 300 BAR 8-Chrome', 'Downtown B\'s Indian Kitchen', 'Nihonshu Genka Sakagura Shinjuku', 
                    'Jiromaru Akihabara', 'Ise Sueyoshi', 'Nabezo Shibuya'], 
                    ['Fratelli Cuore Pizzeria', 'Indian Palace', 'Risorane Taj Palace', 'Gustarium', 'Royal India',
                    'Osteria Vecchio Cancello', 'Tratoria Ponte Cecchio', 'i\' Girone De\' ghiotti', 'Case del Vin Santo',
                    'Deguseria Italiana agli Uffizi'],
                    ['Benihana', 'Goji Kitchen + Bar', 'Sirimahannop', 'Bangkok Halal Kitchen', 'Market Cafe',
                    'Akira Back', 'Ban Khun Mae Restaurant', 'Praya Kichen', 'Riverside Terrace', 'Amristr'],
                    ['"DOC" Cruderia EnoBistrot', 'Bono Bottega Nostrana - San Pietro', 'Rosamuda\'s', 'Vulio', 
                    'Rame Sushi Naturale Italiano', 'Er Pizzicarolo', 'Pinsialy Ttrevi', 'Arrosticinando', 
                    'CiPASSO Bistrot', 'Pizza E Mozzarella'],
                    ['Jaipur Adda', 'The Rajput Room', 'Zolocrust', 'RJ 14', 'Taruveda', 'Chao Chinese Bistro', 'Tapri Central',
                    'Dragon House', 'Handi', 'Somaode Haveli'],
                    ['Lelapa Restaurant', 'Reviere Social Table', 'Mzansi', 'Whole Earth Cafe', 'Homespun',
                    'Chef\'s Warehouse Baeu Constantia', 'La Colombe', 'Osteria Tarantino', 'Alex on Fire Moo Bistro',
                    'Miller\'s Thumb'],
                    ['Manda de Laos', 'Yuni Yupoun Restaurant', 'Two Little Birds Cafe', 'L\'Isola dei Nuroghi Riverview', 
                    'Popolo', '525 Cocktails & Tapas', 'Carpe Diem Restauran', 'Phonheuange Cafe', 'Bouuang', 
                    'Khaiphaen']]
transportations = ['foot', 'road vehicle', 'aircraft', 'watercraft', 'train', 'animal-powered']
lists_entertainments = [['Blue Unicorn Art Exhibit', 'Otomi Grand Prix', 'Acrylic Painting', 'San Miguel Walking Tour', 
                        'Botanical Garden', 'Classical Guitar Concert', 'Tai Chi class', 'Karaoke party', 
                        'Teatro Angela Peralta Theater', 'Gilded Photography'], 
                        ['City Palace of Udaipur', 'Shri Ekling Ji Temple', 'Animal Aid Unlimited', 'Street Food Crawl Tour', 
                        'Countryside Bike Tour', 'Leopard Safari', 'Bagore Ki Haveli Museum'], 
                        ['Bosphorus Sunset Cruise', 'Cappadocia Balloon Ride', 'Whirling Dervish Ceremony', 
                        'Vialand Theme Park', 'Turkish Bath', 'Historic Off the Beaten Path', 'Sultana\'s Belly Dancing', 
                        'Dolmabahce Palace', 'AV Quad Safari', 'Blue Mosque'], 
                        ['Yomiuri Land (Theme Water Park)', 'Meiji Jingu Shrine', 'Shinjuku Gyoen National Garden', 
                        'Edo-Tokyo Museum', 'Tolyo Skytree', 'teamLab Borderless Art Gallery', 'Ryogoku Kokugikan Arena', 
                        'Akasaka Palace', 'Shinjuku Golden Gai', 'Omoide Yoocho Walking Tour'],
                        ['Tuscany Wine Tour', 'Chianti Safari', 'David & Accademia Gallery Tour', 'Duomo Skywalk', 'E-Bike Ride',
                        'Florence Walking Food Tour', 'Cinque Terre Vineyard Hike', 'Chiani Hot Air Balloon Ride',
                        'Gimignano Horseback Ride', 'Florence Aperitivo Time'],
                        ['Bangkok by Night Tour', 'Temple of Dawn (Wat Arun)', 'Jim Thompson House Museum',
                        'Rajadamnern Thai Boxing Stadium', 'Pearl Dinner Cruise', 'Twilight Bamboo Bicycle Tour', 
                        'Erawan Waterfalls', 'Floating Market Damnoen Saduak', 'Chauchak Weekend Market', 
                        'Asiatique The Riverfron'],
                        ['Tour of the Vatican', 'Colosseum Arena Tour', 'Rome Food Tour by Susnset', 'Vespa Tour by Night', 
                        'Pasta & Tiramisu Lovers Workshop', 'Wonders of Vatican Museum', 'Pompeii Day Trip',
                        'Crypt and Catacombs Walking Tour', 'Cooking Class in Piazza Navona', 'Twilight Trasevere Wine Tour'], 
                        ['Safari in Jhalana Leopard Conservation Reserve', 'Taj Mahal', 'Jantar Mantar', 
                        'Hawa Mahal - Palace of Wind', 'Nahargarh Fort', 'Elephant Joy', 'The Rustic Paths',
                        'Akshardham Temple', 'Jaipur by Night', 'Nahargarh Cycle Tour'],
                        ['Shark Cage Diving', 'African Story Wine Tours', 'Table Mountain National Park', 'Seal Snorkling', 
                        'Hopper Helicopter Tour', 'Sunset Champagne Cruise', 'Ocean Wonder', 'SA Four Adventures Ziplining',
                        'Robben Island Tour', 'Penguins Tour'],
                        ['National Museum of Luang Prabang', 'Mekong Cruise', 'Bamboo Weaving Class', 'Bamboo Bridge',
                        'Luang Prabang Night Market', 'The Living Land Farm', 'Mount Phousi', 'MandaLao Elephant Conservation',
                        'Wat Xiengthong', 'Kuang Si Falls Butterfly Park']]
selected_names, lists_names = [], ["destinations", "restaurants", "transportations", "entertainments"]


# Function to show greeting upon starting planner.
def show_greeting():
    print("Welcome to the Day Trip Planner. Let's plan your next trip!\n")
    run_planner()
    

# Function to run planner.
def run_planner():
    get_initial_values()
    confirm_initial_values()


# Function to get initial values for the trip.
def get_initial_values():
    get_destination()
    get_restaurant()
    get_transportation()
    get_entertainment()


# Function to select destination.
def get_destination():
    while len(selected_names) == 0:
        random_destination = get_random_value(destinations)
        question = f"Destination: Would you like to visit {random_destination}? (Type n, y, no, yes): "
        evaluate_user_input(random_destination, "destination", question, input(question).lower())


# Function to select restaurant.
def get_restaurant():    
    while len(selected_names) == 1 or selected_names[1] == "None":
        random_restaurant = get_random_value(lists_restaurants[destinations.index(selected_names[0])])
        question = f"Restaurant: Would you like to eat at {random_restaurant}? (Type n, y, no, yes): "
        evaluate_user_input(random_restaurant, "restaurant", question, input(question).lower())


# Function to select transportation.
def get_transportation():
    while len(selected_names) == 2 or selected_names[2] == "None":
        random_transportation = get_random_value(transportations)
        question = f"Transportation: Would you like to travel by {random_transportation}? (Type n, y, no, yes): "
        evaluate_user_input(random_transportation, "transportation", question, input(question).lower())


# Function to select form of entertainment.
def get_entertainment():
    while len(selected_names) == 3 or selected_names[3] == "None":
        random_entertainment = get_random_value(lists_entertainments[destinations.index(selected_names[0])])
        question = f"Entertianment: Would you to spend time at the {random_entertainment}? (Type n, y, no, yes): "
        evaluate_user_input(random_entertainment, "entertainment", question, input(question).lower())


# Function to get random name from current list. // CONSIDER using shuffle and subscripting based on length of list and counter
# for get_destination(), get_restaurant(), get_transportation() and get_entertainment() or using numpy as np to create an array
# and subscript. Need to load numpy module, try:
#
# def get_random_value(current_list, n=0)
#     np.random.permutation(current_list)
#     random_item = current_list[n]
#     if n == len(current):
#         n = 0
def get_random_value(current_list):
    return random.choice(current_list)


# Function to evaluate user's input. // Break up into evaluate_user_input_no & evaluate_user_input_yes
def evaluate_user_input(random_item, list_name, question, user_input, n=-1):
    n = int(n)
    while len(user_input) == 0:
        user_input = input(question).lower()
    if user_input in ('y', 'yes') and list_name == "Check":
        return n
    elif user_input in ('n', 'no') and list_name == "Check":
        if n == 0:
            selected_names.clear()
        elif n > 0:
            selected_names[n] = "None"
        run_planner()
    elif user_input in ('y', 'yes') and list_name == "Confirmation":
        get_confirmation()
    elif user_input in ('n', 'no') and list_name == "Confirmation":
        get_modified_values()
    elif user_input in ('y', 'yes'):
        if n == -1:
            if "None" in selected_names:
                selected_names[selected_names.index("None")] = random_item
            else:     
                selected_names.append(random_item)
        elif n > -1:
            selected_names[n] = random_item
        show_selection(list_name, random_item)
    elif user_input in ('n', 'no'):
        get_initial_values()


# Function to show confirmation of value selection.
def show_selection(list_name, random_item):
    print(f"You have selected {random_item} as your {list_name}!\n")


# Function to confirm inital values.
def confirm_initial_values():
    question = f"\nPlease Confirm\n\nWe have you arriving at {selected_names[0]} today, travelling by {selected_names[2]}, eating"\
               f" at {selected_names[1]}, and spending time at {selected_names[3]}. Is this right? (Type n, y, no, yes):"
    user_input = input(question)
    evaluate_user_input("Item", "Confirmation", question, user_input)


# Function to print confirmation.
def get_confirmation():
    print(f"\nConfirmation\n\nWe are happy to confirm you will be arriving at {selected_names[0]} by {selected_names[2]}, eating "
          f"at the grand {selected_names[1]} and spending time at {selected_names[3]}. We hope you enjoy! Thank you for booking "
          f"with us!\n")
    exit()


# Function to modify user's original selections. // WHY?
def get_modified_values():
    get_modify_destination()
    get_modify_restaurant()
    get_modify_transportation()
    get_modify_entertainment()
    confirm_initial_values()


# Function to get modification to destination.
def get_modify_destination():
    ndex_list = 0
    while ndex_list < 1:
        question = f"\nDo you still want to visit {selected_names[0]}? (Type y, n, yes, or no): "
        evaluate_user_input(selected_names[0], "Check", question, input(question), ndex_list)
        ndex_list += 1
        

# Function to get modification to restaurant.
def get_modify_restaurant():
    ndex_list = 1
    while ndex_list < 2:
        question = f"\nDo you still want to eat at {selected_names[1]}? (Type y, n, yes, or no): "    
        evaluate_user_input(selected_names[1], "Check", question, input(question), ndex_list) 
        ndex_list += 1 


# Functtion to get modification to transportation.
def get_modify_transportation():
    ndex_list = 2
    while ndex_list < 3: 
        question = f"\nDo you still want to travel by {selected_names[2]}? (Type y, n, yes, or no): "
        evaluate_user_input(selected_names[2], "Check", question, input(question), ndex_list)
        ndex_list += 1


# Function to get modification to entertainment.
def get_modify_entertainment():
    ndex_list = 3
    while ndex_list < 4: 
        question = f"\nDo you still want to spend time at {selected_names[3]}? (Type y, n, yes, or): "
        evaluate_user_input(selected_names[3], "Check", question, input(question), ndex_list)
        ndex_list += 1


# Start program
show_greeting()
