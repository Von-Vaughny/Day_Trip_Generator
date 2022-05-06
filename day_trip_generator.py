import random


# Function to capture 
def san_miguel_de_allende():
    allende_dict = {'restaurants': ['La Doña de San Miguel', 'Rustica', 'Hecho en Mexico', 'The Restaurant', 'Lavanda Cafe',
        'Restaurante 1826','Trazo 1810', 'Marsala', 'El Rinconcito', 'Carajillo San Miguel'],
                    'entertainments': ['Blue Unicorn Art Exhibit', 'Otomi Grand Prix', 'Acrylic Painting', 'San Miguel Walking Tour', 
                    'Botanical Garden', 'Classical Guitar Concert', 'Tai Chi class', 'Karaoke party', 'Teatro Angela Peralta Theater', 
                    'Gilded Photography']}
    return allende_dict


def udaipur():
    udaipur_dict = {'restaurants': ['Raaj Bagh', 'Restaurant Harigarh', 'Aravali Lakview', 'Syah', 'Skyfall Rooftop Restaurant', 
        'SABOR World Cuisine', 'Jaajam Restaurant', 'Kotra Haveli Roof Top Restaurant & Cafef', 'Jaiwana Haveli Roof Top', 
        'Helloboho Lake Side Restaurant'],
                    'entertainments': ['City Palace of Udaipur', 'Shri Ekling Ji Temple', 'Animal Aid Unlimited', 
                    'Street Food Crawl Tour', 'Countryside Bike Tour', 'Leopard Safari', 'Bagore Ki Haveli Museum']}
    return udaipur_dict


# Function to capture destinations. 
def get_destinations():
    destinations = ['San Miguel De Allende', 'Udaipur']
    return destinations

# Function to randomly select a destination.
def random_destination(destinations):
    return random.choice(destinations)


# Function to pick data from user selected destination.
def get_destination_data(destination):
    return globals()[destination]()


# Function to get restaurants from user selected destination.
def get_restaurants(destination):
    destination_data = get_destination_data(destination)
    return destination_data['restaurants']
    

# Function to randomly select a restaurant from user selected destination.
def random_restaurants(destination):
    restaurants = get_restaurants(destination)
    return random.choice(restaurants)


# Function to randomly select a mode of transportation from user selected destination.
def random_transportation():
    transportations = ['feet', 'road vehicle', 'aircraft', 'watercraft', 'train', 'animal-powered']
    return random.choice(transportations)


# Function to get entertainments from user selected destination.
def get_entertainments(destination):
    destination_data = get_destination_data(destination)
    return destination_data['entertainment']


# Function to randomly select entertainment from user selected destination.
def random_entertainment(destination):
    entertainments = get_entertainments(destination)
    return random.choice(entertainments)


def next_action(destinations, destination, s_destination, s_restaurant, s_transportation, s_entertainment):
    if len(s_destination) < 1:
        random_value = random_destination(destinations)
    elif len(s_restaurant) < 1: 
        random_value = random_restaurants(destination)
    elif len(s_transportation) < 1:
        random_value = random_transportation()
    elif len(s_entertainment) < 1:
        random_value = random_entertainment(destination)
    return random_value


# Function to determine question to ask user.
def select_question(random_value, destinations, destination):
    if random_value in (destinations):
        question = f"Would you like to visit {random_value}? (Type y, n, yes, or no)"
    elif random_value in get_restaurants(destination):
        question = f"Would you like to eat at {random_value}? (Type y, n, yes, or no)"
    elif random_value in ['feet', 'road vehicle', 'aircraft', 'watercraft', 'train', 'animal-powered']:
        question = f"Would you like to travel by {random_value}? (Type y, n, yes, or no)"
    elif random_value in get_entertainments(destination):
        question = f"Would you like to spend time at the {random_value}? (Type y, n, yes, or no)"
    return question


# Function to get question and user's input.
def get_user_input(destinations, destination, s_destination, s_restaurant, s_transportation, s_entertainment):
    random_value = next_action(destinations, destination, s_destination, s_restaurant, s_transportation, s_entertainment)
    question = select_question(random_value, destinations, destination)
    return question, input(question)


# Function to evaluate user's input.
def evaluate_user_input(question, user_input):
    while len(user_input) == 0 or user_input not in ('y', 'n', 'yes', 'no'):
        user_input = input(question)
    


def main():
    destinations = get_destinations()
    destination, s_destination, s_restaurant, s_transportation, s_entertainment = '', '', '', '', ''

    while True:
        question, user_input = get_user_input(destinations, destination, s_destination, s_restaurant, s_transportation, s_entertainment)
        evaluate_user_input(question, user_input)



main()