import math
from copy import deepcopy

def total_worth(houses):
    """
    Calculates the total worth of the neighbourhood
    """
    total_value = 0
    for house in houses:
        total_value = total_value + house.worth
    return total_value


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