import random
from copy import deepcopy
from code.classes.Amstelhaege import Amstelhaege

def hillclimber2(amstelhaege):
    """
    This version of hillclimber starts with a random solution. Then each house 
    is moved in a random direction (steps of 1m). If this move increases the area worth,
    we keep moving the house in this direction, until the worth starts decreasing. 
    """
    directions = ["up", "down", "right", "left"]
    for house in amstelheage.houses:
        direction = random.choice(directions)
        amstelheage.get_free_space()
        worth = amstelhaege.calculate_worth()
        new_worth = amstelheage.calculate_worth()
        while new_worth >= worth:
            previous_step_house = deepcopy(house)
            previous_step_worth = new_worth
            # previous_step_amstelhaege = deepcopy(amstelhaege)
            new_coordinates = hillclimber2_move(house, direction)

            house.x_left = new_coordinates[0]
            house.x_right = new_coordinates[1]
            house.y_bottom = new_coordinates[2]
            house.y_top = new_coordinates[3]

            amstelhaege.get_free_space()
            new_worth = amstelheage.calculate_worth()
    
            # change the coordinates back, when the move decreases the worth
            if new_worth < worth:
                house.x_left = previous_step_house.x_left
                house.x_right = previous_step_house.x_right
                house.y_bottom = previous_step_house.y_bottom
                house.y_top = previous_step_house.y_top
                new_worth = previous_step_worth 
                # amstelhaege = previouw.step_amstelhaege 
    
    return amstelhaege, new_worth


def hillclimber2_move(house, direction):
    # coordinates in new coordinates: [x_left, x_right, y_bottom, y_top]
    if direction == "up":
        new_coordinates = [house.x_left, house.x_right, house.y_bottom + 1, house.y_top + 1]
    elif direction == "down":
        new_coordinates = [house.x_left, house.x_right, house.y_bottom - 1, house.y_top - 1]
    elif direction == "right":
        new_coordinates = [house.x_left + 1, house.x_right + 1, house.y_bottom, house.y_top]
    elif direction == "left": 
        new_coordinates = [house.x_left - 1, house.x_right - 1, house.y_bottom, house.y_top]

    return new_coordinates


