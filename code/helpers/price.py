def calculate_price(neighbourhood):
    """
    function that calculates the price of the entire neighbourhood
    """

    price = 0

    # loops through all the houses in the neighbourhood
    for house in neighbourhood:
        if house.name != 'water':
            # calculates the new price of the house 
            house.price = house.value * (1 + house.increase_value * ("house.minimum_distance" - house.free_area))

            # add price to neighbourhood price
            price += house.price
    
    return price

def minimum_distance(neighbourhood):
    """
    function that calculates the minimum distance between houses
    """
    






