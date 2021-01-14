import random
from copy import deepcopy
from code.classes.Amstelhaege import Amstelhaege
from code.algorithms.random import random
import time
from random import shuffle, choice

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
        timeout_start = time.time()
        while time.time() < timeout_start + timeout:
            # for house in self.amstelhaege.houses:
            house = choice(self.amstelhaege.houses)
            shuffle(self.directions)
            new_price = self.amstelhaege.price + 1
            for direction in self.directions:
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

                    new_price = self.get_price()
                
                    if new_price < old_price:
                        house.move(initial_x, initial_y)
                        self.amstelhaege.get_free_space()
                        self.amstelhaege.calculate_worth()

        return self.amstelhaege

    # def find_best_direction(self, house):
    #     best_direction = None
    #     for direction in self.directions:
    #         x = house.x_left
    #         y = house.y_bottom

    #         old_price = self.get_price()
    #         new_coordinates = self.hillclimber2_move(house, direction)

    #         house.move(-100, -100)
            
    #         if self.amstelhaege.check_location(new_coordinates[0], new_coordinates[1], house.width, house.length, house.free_area):
    #             house.move(new_coordinates[0], new_coordinates[1])
    #         else: 
    #             house.move(x, y)

    #         new_price = self.get_price()
        
    #         if new_price < old_price:
    #             house.move(x, y)
    #         elif new_price > old_price:
    #             best_direction = direction
        

    #     return best_direction

    # def run(self, timeout):
    #     random(self.amstelhaege)
    #     timeout_start = time.time()
    #     while time.time() < timeout_start + timeout:
    #         # for house in self.amstelhaege.houses:
    #         house = choice(self.amstelhaege.houses)
    #         old_price = self.amstelhaege.price
    #         new_price = self.amstelhaege.price + 1
        
    #         while new_price > old_price:
    #             old_price = self.get_price()
    #             best_direction = self.find_best_direction(house)
    #             if best_direction is not None:
    #                 best_coordinates = self.hillclimber2_move(house, best_direction)
    #                 house.move(best_coordinates[0], best_coordinates[1])
    #             new_price = self.get_price()
    #             # print(f"house{house.id} best dir {best_direction}")
    
    #     return self.amstelhaege
