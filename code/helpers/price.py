import math
from copy import deepcopy

def worth(houses):
    """
    Calculates the worth of the neighbourhood
    """

    total_value = 0
    for houses in houses_list:
        total_value = total_value + house



def calculate_price(houses):
    """
    function that calculates the price of the entire neighbourhood
    """

    price = 0

    # loops through all the houses in the neighbourhood
    for house in houses:
        # calculates the new price of the house 
        house.price = house.value * (1 + house.increase_value * (house.total_freearea - house.free_area))

        # add price to neighbourhood price
        price += house.price
    
    return price