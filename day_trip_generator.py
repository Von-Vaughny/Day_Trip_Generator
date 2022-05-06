import random


# Function to capture 
def san_miguel_de_allende():
    restaurants = ['La Doña de San Miguel', 'Rustica', 'Hecho en Mexico', 'The Restaurant', 'Lavanda Cafe','Restaurante 1826',
        'Trazo 1810', 'Marsala', 'El Rinconcito', 'Carajillo San Miguel']
    entertainments = ['Blue Unicorn Art Exhibit', 'Otomi Grand Prix', 'Acrylic Painting', 'San Miguel Walking Tour', 
                    'Botanical Garden', 'Classical Guitar Concert', 'Tai Chi class', 'Karaoke party', 'Teatro Angela Peralta Theater', 
                    'Gilded Photography']
    return restaurants, entertainments


def udaipur():
    restaurants = ['Raaj Bagh', 'Restaurant Harigarh', 'Aravali Lakview', 'Syah', 'Skyfall Rooftop Restaurant', 'SABOR World Cuisine', 
        'Jaajam Restaurant', 'Kotra Haveli Roof Top Restaurant & Cafef', 'Jaiwana Haveli Roof Top', 'Helloboho Lake Side Restaurant']
    entertainments = ['City Palace of Udaipur', 'Shri Ekling Ji Temple', 'Animal Aid Unlimited','Street Food Crawl Tour',
        'Countryside Bike Tour', 'Leopard Safari', 'Bagore Ki Haveli Museum']
    return restaurants, entertainments


# Function to capture destinations. 
def get_destinations():
    return ['San Miguel De Allende', 'Udaipur']


def get_restaurants_entertainments(selected_names):
    city = selected_names[0].lower().replace(' ', '_')
    restaurants, entertainments = globals()[city]() 
    return restaurants, entertainments


# Function to get the name of the next random value in the current list. / FIX restaurants and entertainments
def check_for_list(selected_names, destinations, transportations):
    if len(selected_names) == 0:
        current_list = destinations
    elif len(selected_names) == 1 or len(selected_names) > 1 and selected_names[1] == "None":
        current_list = get_restaurants_entertainments(selected_names)[0]
    elif len(selected_names) == 2 or len(selected_names) > 2 and selected_names[2] == 'None':
        current_list = transportations
    elif len(selected_names) == 3 or len(selected_names) > 3 and selected_names[3] == 'None':
        _, current_list = get_restaurants_entertainments(selected_names)
    return current_list


# Function to randomly select item in current_list.
def random_pick(current_list):
    return random.choice(current_list)


# Function to get 
def select_question(list_item_name, destinations, transportations, selected_names):
    if list_item_name in destinations:
        question = f"Would you like to visit {list_item_name}? (Type y, n, yes, or no)"
    if len(selected_names) > 0:
        restaurants, entertainments = get_restaurants_entertainments(selected_names)  
        if list_item_name in restaurants:
            question = f"Would you like to eat at {list_item_name}? (Type y, n, yes, or no)"
        elif list_item_name in transportations:
            question = f"Would you like to travel by {list_item_name}? (Type y, n, yes, or no)"
        elif list_item_name in entertainments:
            question = f"Would you like to spend time at the {list_item_name}? (Type y, n, yes, or no)"
    return question

    
def next_list_value(selected_names, destinations, transportations):
    current_list = check_for_list(selected_names, destinations, transportations)
    return random_pick(current_list)


# Function to get user input.
def get_user_input(selected_names, destinations, transportations):    
    list_item_name = next_list_value(selected_names, destinations, transportations)
    question = select_question(list_item_name, destinations, transportations, selected_names)
    return list_item_name, question, input(question + " ")


def remove_list_item_name(selected_names, list_item_name, destinations, transportations):
    current_list = check_for_list(selected_names, destinations, transportations)
    return current_list.remove(list_item_name)


def check_list(selected_names, destinations, transportations):
    current_list = check_for_list(selected_names, destinations, transportations)
    if len(current_list) == 0:
        print('alert')


def evaluate_user_input(user_input, question, list_item_name, selected_names, destinations, transportations):
    while len(user_input) == 0 or user_input not in ('y', 'n', 'yes', 'no'):
        user_input = input(question)
    if user_input in ('n', 'no'):
        remove_list_item_name(selected_names, list_item_name, destinations, transportations)
        check_list(selected_names, destinations, transportations)
    elif user_input in ('y', 'yes'):
        selected_names.append(list_item_name)


def main():
    transportations = ['feet', 'road vehicle', 'aircraft', 'watercraft', 'train', 'animal-powered']
    selected_names, restaurants, entertainments = [], [], []
    destinations = get_destinations()
    while True:
        list_item_name, question, user_input = get_user_input(selected_names, destinations, transportations)
        evaluate_user_input(user_input, question, list_item_name, selected_names, destinations, transportations)


if __name__ == "__main__":
    main()