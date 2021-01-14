import random
from copy import deepcopy
from code.classes.Amstelhaege import Amstelhaege
from code.algorithms.random import random
import time
from random import shuffle

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
        # coordinates in new coordinates: [x_left, y_bottom]
        if direction == "up":
            self.new_coordinates = [house.x_left, house.y_bottom + 1]
        elif direction == "down":
            self.new_coordinates = [house.x_left, house.y_bottom - 1]
        elif direction == "right":
            self.new_coordinates = [house.x_left + 1, house.y_bottom]
        elif direction == "left": 
            self.new_coordinates = [house.x_left - 1, house.y_bottom]

        return self.new_coordinates
    
    def get_price(self):
        self.amstelhaege.get_free_space()
        self.amstelhaege.calculate_worth()
        return self.amstelhaege.price

    def run(self, timeout):
        random(self.amstelhaege)
        old_price = self.amstelhaege.price
        #new_price = self.amstelhaege.price + 1
        timeout_start = time.time()
        while time.time() < timeout_start + timeout:
            for house in self.amstelhaege.houses:
                shuffle(self.directions)
                new_price = self.amstelhaege.price + 1
                #print(self.directions)
                for direction in self.directions:
                    #print(f"{house.id} direction {direction}")
                    while new_price > old_price:
                        initial_x = house.x_left
                        initial_y = house.y_bottom
                        old_price = self.get_price()
                        new_coordinates = self.hillclimber2_move(house, direction)

                        house.move(-100, -100)
                        
                        if self.amstelhaege.check_location(new_coordinates[0], new_coordinates[1], house.width, house.length, house.free_area):
                            house.move(new_coordinates[0], new_coordinates[1])
                        else: 
                            house.move(initial_x, initial_y)
                        #print(f"house {house.id} coordinates {house.x_left} {house.y_bottom}")
                        new_price = self.get_price()
                    
                        if new_price < old_price:
                            house.move(initial_x, initial_y)
                            self.amstelhaege.get_free_space()
                            self.amstelhaege.calculate_worth()
        
        return self.amstelhaege

