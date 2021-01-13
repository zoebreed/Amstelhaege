from copy import deepcopy
from random import randrange, choice
from code.algorithms.random_placement import random_placement, random_algorithm
import time

class Hillclimber_1:
    """
    Executes the first version of the hillclimber algorithm.
    First the houses are places randomly. Then a random house
    is placed at a random location. If this random location 
    increases the total price, it stays. If this random location
    decreases the total price, we remove it.
    """
    def __init__(self, amstelhaege):
        self.amstelhaege = deepcopy(amstelhaege)

    def move_house_random(self, house):
        """
        runs until available coordinates are found randomly and the house is places
        """
        while True:
            x = randrange(self.amstelhaege.length)
            y = randrange(self.amstelhaege.width)

            # check if the random coordinates are available
            if self.amstelhaege.check_location(x, y, house.length, house.width, house.free_area):
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
        
        # places the houses at a random location
        random_placement(self.amstelhaege)

        timeout_start = time.time()

        # stop if the total price converges
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

        return self.amstelhaege, self.amstelhaege.price