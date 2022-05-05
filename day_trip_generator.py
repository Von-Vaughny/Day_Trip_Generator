import random


# Function to capture 
def san_miguel_de_allende():
    restaurants = ['La Doña de San Miguel', 'Rustica', 'Hecho en Mexico', 'The Restaurant', 'Lavanda Cafe', 'Restaurante 1826', 
        'Trazo 1810', 'Marsala', 'El Rinconcito', 'Carajillo San Miguel']
    entertainment = ['Blue Unicorn Art Exhibit', 'Otomi Grand Prix', 'Acrylic Painting', 'San Miguel Walking Tour', 'Botanical Garden',
        'Classical Guitar Concert', 'Tai Chi', 'Karaoke', 'Teatro Angela Peralta Theater', 'Gilded Photography']
    return restaurants, entertainment


def udaipur():
    restaurants = ['Raaj Bagh', 'Restaurant Harigarh', 'Aravali Lakview', 'Syah', 'Skyfall Rooftop Restaurant', 'SABOR World Cuisine'
        'Jaajam Restaurant', 'Kotra Haveli Roof Top Restaurant & Cafef', 'Jaiwana Haveli Roof Top', 'Helloboho Lake Side Restaurant']
    entertainment = ['City Palace of Udaipur', 'Shri Ekling Ji Temple', 'Animal Aid Unlimited', 'Street Food Crawl', 
        'Countryside Bike Tour', 'Leopard Safari', 'Bagore Ki Haveli Museum']
    return restaurants, entertainment


# Function to capture destinations. 
def get_destinations():
    destinations = ['San Miguel De Allende', 'Udaipur']
    return destinations


# Function to randomly select a destination.
def random_destination(destinations):
    destination = random.choice(destinations)
    return destination


# Function to capture user's decision on destination.
def get_user_destination_input(destinations):
    destination = random_destination(destinations)
    user_input = input(f"Would you like to visit {destination}? (Type y, n, yes, or no) ")
    return destination, user_input
    

# Function to remove randomly selected destination from destinations. 
def remove_destination(destinations, destination):
    destinations.remove(destination)
    

# Function to evaluate user's decision on destination.
def user_destination_input_evaluate(destinations):
    destination, user_input = get_user_destination_input(destinations)
    while len(user_input) < 1 or user_input not in ('y', 'n', 'yes', 'no'):
        user_input = input(f"Would you like to visit {destination}? (Type y, n, yes, or no) ")
    if user_input in ('n', 'no'):
        remove_destination(destinations, destination)
        user_destination_input_evaluate(destinations)



def main():
    destinations = get_destinations()
    user_destination_input_evaluate(destinations)


if __name__ == "__main__":
    main()
