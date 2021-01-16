from copy import deepcopy
from random import randrange, choice
import time
import math
from code.algorithms.simulated_annealing import Simulated_annealing

from random import uniform, randrange, random

class Hillclimber_1:
    """
    Executes the first version of the hillclimber algorithm.
    First the houses are places randomly. Then a random house
    is placed at a random location. If this random location 
    increases the total price, it stays. If this random location
    decreases the total price, we remove it.
    """
    def __init__(self, amstelhaege, sim_ann=False):
        self.amstelhaege = amstelhaege

        # if the user chose with simulated annealing, initialize
        if sim_ann:
            self.simulated_annealing = Simulated_annealing()
            self.condition = lambda: self.simulated_annealing.get_condition()
            self.price_check = lambda a: self.simulated_annealing.check_price(a)

        else:
            self.iterations = 1000
            self.condition = lambda: self.get_condition()
            self.price_check = lambda a: self.check_price(a)

    def move_house_random(self, house):
        """
        runs until available coordinates are found randomly and the house is places
        """
        while True:
            x = randrange(self.amstelhaege.width)
            y = randrange(self.amstelhaege.length)

            # check if the random coordinates are available
            if self.amstelhaege.check_location(x, y, house.width, house.length, house.free_area):
                house.move(x,y)
                return
        

    def price_diff(self):
        """
        returns the price difference
        """

        self.amstelhaege.get_free_space()
        self.amstelhaege.calculate_worth()

        return self.amstelhaege.price - self.old_price

    def get_condition(self):
        """
        simple for loop implementation
        """
        
        if self.iterations == 0:
            return False

        self.iterations -= 1
        
        return True

    def check_price(self, price_diff):
        """
        returns True when the old price was higher, else False
        """
        
        if price_diff < 0:
            return True
        return False


    def run(self):
        
        while self.condition():
            
            self.old_price = self.amstelhaege.price
            
            # get a random house
            house = choice(self.amstelhaege.houses)

            # save the original coordinates for later
            x, y = house.x_left, house.y_bottom

            # move the house temporarily outside of the map to prevent overlap on itself
            house.move(-100, -100)

            # move the house to a random location within the map
            self.move_house_random(house)

            # get the difference between the old and new price
            price_diff = self.price_diff()

            # accept the change if the price is higher, else change back the coordinates
            if self.price_check(price_diff):

                house.move(x, y)
                self.amstelhaege.get_free_space()
                self.amstelhaege.calculate_worth()

        return self.amstelhaege