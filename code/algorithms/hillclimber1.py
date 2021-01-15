from copy import deepcopy
from random import randrange, choice
import time
import math
from random import uniform, randrange

class Hillclimber_1:
    """
    Executes the first version of the hillclimber algorithm.
    First the houses are places randomly. Then a random house
    is placed at a random location. If this random location 
    increases the total price, it stays. If this random location
    decreases the total price, we remove it.
    """
    def __init__(self, amstelhaege):
        self.amstelhaege = amstelhaege

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

    def check_price(self, old_price):
        """
        returns True when the new price is higher, False otherwise
        """

        self.amstelhaege.get_free_space()
        self.amstelhaege.calculate_worth()

        if self.amstelhaege.price > old_price:
            return True
        return False

    def run(self, timeout):
        
        # # places the houses at a random location
        # random(self.amstelhaege)

        timeout_start = time.time()

        # stop if the given time has passed
        while time.time() < timeout_start + timeout:
            
            old_price = self.amstelhaege.price
            
            # get a random house
            house = choice(self.amstelhaege.houses)

            # save the original coordinates for later
            x, y = house.x_left, house.y_bottom

            # move the house temporarily outside of the map to prevent overlap on itself
            house.move(-100, -100)

            # move the house to a random location within the map
            self.move_house_random(house)

            # accept the change if the price is higher, else change back the coordinates
            if not self.check_price(old_price):

                house.move(x,y)
                self.amstelhaege.get_free_space()
                self.amstelhaege.calculate_worth()

        return self.amstelhaege

    def run_sa(self):
        """
        runs the same hillclimber version 1 algorithm but with simulated annealing
        """
        # initialize the temperature
        initial_temp = 900
        final_temp = .1
        alpha = 0.01
        current_temp = initial_temp

        # places the houses at a random location
        random(self.amstelhaege)

        # stop if the given time has passed
        while current_temp > initial_temp:
            
            old_price = self.amstelhaege.price
            
            # get a random house
            house = choice(self.amstelhaege.houses)

            # save the original coordinates for later
            x, y = house.x_left, house.y_bottom

            # move the house temporarily outside of the map to prevent overlap on itself
            house.move(-100, -100)

            # move the house to a random location within the map
            self.move_house_random(house)

            # accept the change if the price is higher, else change back the coordinates
            if not self.check_price(old_price):
                
                price_diff = old_price - self.amstelhaege.price

                if  not uniform(0, 1) < math.exp(price_diff / current_temp):
                    house.move(x,y)
                    self.amstelhaege.get_free_space()
                    self.amstelhaege.calculate_worth()

            current_temp -= alpha

        return self.amstelhaege

