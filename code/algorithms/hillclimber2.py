import random
from copy import deepcopy
from code.classes.Amstelhaege import Amstelhaege

class Hillclimber_2:
    """
    This version of hillclimber starts with a random solution. Then each house 
    is moved in a random direction (steps of 1m). If this move increases the area worth,
    we keep moving the house in this direction, until the worth starts decreasing. 
    """
    def __init__(self, amstelhaege):
        self.amstelhaege = deepcopy(amstelhaege)
        self.directions = ["up", "down", "right", "left"]
    
    def hillclimber2_move(self, house, direction):
        # coordinates in new coordinates: [x_left, x_right, y_bottom, y_top]
        if direction == "up":
            self.new_coordinates = [house.x_left, house.x_right, house.y_bottom + 1, house.y_top + 1]
        elif direction == "down":
            self.new_coordinates = [house.x_left, house.x_right, house.y_bottom - 1, house.y_top - 1]
        elif direction == "right":
            self.new_coordinates = [house.x_left + 1, house.x_right + 1, house.y_bottom, house.y_top]
        elif direction == "left": 
            self.new_coordinates = [house.x_left - 1, house.x_right - 1, house.y_bottom, house.y_top]

        return self.new_coordinates
    
    def get_price(self):
        self.amstelhaege.get_free_space()
        self.amstelhaege.calculate_worth()
        return self.amstelhaege.price

    def run(self):
        random_placement(self.amstelhaege)
        old_price = self.amstelhaege.price
        new_price = self.amstelhaege.price
        timeout_start = time.time()
        while time.time() < timeout_start + timeout:
            for house in self.amstelheage.houses:
                direction = random.choice(directions)
                while new_price >= old_price:
                    initial_house = deepcopy(house)
                    old_price = self.get_price()
                    new_coordinates = self.hillclimber2_move(house, direction)

                    house.x_left = new_coordinates[0]
                    house.x_right = new_coordinates[1]
                    house.y_bottom = new_coordinates[2]
                    house.y_top = new_coordinates[3]

                    new_price = self.get_price()
                
                    if new_price < old_price:
                        house.move(initial_house.x_left, initial_house.y_bottom)
                        self.amstelhaege.get_free_space()
                        self.amstelhaege.calculate_worth()
        
        return self.amstelhaege


  

