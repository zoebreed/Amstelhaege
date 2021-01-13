from copy import deepcopy
from random import randrange
from code.algorithms.random_placement import random_placement, random_algorithm
import time

def hillclimber1(amstelhaege):
    """
    Executes the first version of the hillclimber algorithm.
    First the houses are places randomly. Then a random house
    is placed at a random location. If this random location 
    increases the total price, it stays. If this random location
    decreases the total price, we remove it.
    
    """

    random_placement(amstelhaege)
    amstelhaege.get_free_space()
    amstelhaege.calculate_worth()

    timeout = 100    
    timeout_start = time.time()

    # stop if the total price converges
    while time.time() < timeout_start + timeout:
        amstelhaege_copy = deepcopy(amstelhaege)
        
        # get a random house
        house_index = randrange(amstelhaege_copy.total)
        neighbourhood_index = amstelhaege.neighbourhood.index(amstelhaege.houses[house_index])
        house = deepcopy(amstelhaege.houses[house_index])

        # delete it from the copy
        del amstelhaege_copy.houses[house_index]
        del amstelhaege_copy.neighbourhood[neighbourhood_index]

        # place the house at a random valid position
        while True:

            x = randrange(amstelhaege_copy.length)
            y = randrange(amstelhaege_copy.width)

            if amstelhaege_copy.check_location(x, y, house.length, house.width, house.free_area):
                amstelhaege_copy.place_house(house.house_type, x, y)
                break

        amstelhaege_copy.get_free_space()
        amstelhaege_copy.calculate_worth()

        # if the new price is higher...
        if amstelhaege_copy.price > amstelhaege.price:
            
            del amstelhaege.houses[house_index]
            del amstelhaege.neighbourhood[neighbourhood_index]
            amstelhaege.place_house(house.house_type, x, y)
            amstelhaege.get_free_space()
            amstelhaege.calculate_worth()
            print(amstelhaege.price)

    return amstelhaege, amstelhaege.price





