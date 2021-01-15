import random
from copy import deepcopy
from code.classes.Amstelhaege import Amstelhaege
import time
from random import shuffle, choice

class Hillclimber_2:
    """
    This version of hillclimber starts with a random solution. The directions list is 
    shuffled for each random house. And then the house is moved in every direction respectively 
    to the list (steps of 1m). If this move increases the area worth, we keep moving the 
    house in this direction, until the worth starts decreasing. 
    """
    
    def __init__(self, amstelhaege):
        self.amstelhaege = amstelhaege
        self.directions = ["up", "down", "right", "left"]
    
    def hillclimber2_move(self, house, direction):
        """
        Returns the x_left and y_bottom coordinates according to the direction
        """
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
        """
        Returns the price of Amstelhaege
        """
        self.amstelhaege.get_free_space()
        self.amstelhaege.calculate_worth()
        return self.amstelhaege.price

    def run(self, timeout):

        # # uses random algorithm to generate the first state
        # random(self.amstelhaege)
        old_price = self.amstelhaege.price

        timeout_start = time.time()

        # stop if the given time has passed
        while time.time() < timeout_start + timeout:
            # for house in self.amstelhaege.houses:
            house = choice(self.amstelhaege.houses)

            # shuffle the direction list to avoid a bias
            shuffle(self.directions)

            # go through every direction in the list
            for direction in self.directions:

                # make sure that at the start of each house and each direction you get in the while loop 
                new_price = self.amstelhaege.price + 1

                # keep stepping into the same direction if the move increases the worth
                while new_price > old_price:
                    # save the initial coordinates
                    x = house.x_left
                    y = house.y_bottom

                    # get the initial price
                    old_price = self.get_price()

                    new_coordinates = self.hillclimber2_move(house, direction)

                    # move the house temporarily outside of the map to prevent overlap on itself
                    house.move(-100, -100)
                    
                    # make the move, if the move is possible. Ohterwise keep the initial place
                    if self.amstelhaege.check_location(new_coordinates[0], new_coordinates[1], house.width, house.length, house.free_area):
                        house.move(new_coordinates[0], new_coordinates[1])
                    else: 
                        house.move(x, y)

                    new_price = self.get_price()

                    # move decreases the worth
                    if new_price < old_price:
                        house.move(x, y)

                    #print(f"house.id {house.id} highest score{new_price} current score {self.get_price()}")

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
            # best_direction = self.find_best_direction(house)
        
    #         while new_price > old_price:
    #             old_price = self.get_price()
    #             if best_direction is not None:
    #                 best_coordinates = self.hillclimber2_move(house, best_direction)
    #                 house.move(best_coordinates[0], best_coordinates[1])
    #             new_price = self.get_price()
    #             # print(f"house{house.id} best dir {best_direction}")
    
    #     return self.amstelhaege
