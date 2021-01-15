from code.classes.Amstelhaege import House
from random import randrange
from copy import deepcopy
from user_input import User
from code.helpers.price import total_worth
from code.classes.Amstelhaege import Amstelhaege
from code.helpers.price import calculate_price
import time

class Random_greedy():
    """
    function that tries to place the house in random locations and places it on the
    best position for the specific house
    """

    def __init__(self, amstelhaege):
        self.amstelhaege = deepcopy(amstelhaege)
        self.highest_score = None
        self.score = None    

    def run(self):
        total = self.amstelhaege.total
        timeout_start = time.time()
        while time.time() < timeout_start + timeout:

            # calculate number of houses for each house type to be placed
            number_eengezinswoning = self.amstelhaege.fraction_house_1 * total
            number_bungalow = self.amstelhaege.fraction_house_2 * total
            number_maison = ((self.amstelhaege.fraction_house_3 * total))
                
            # consider 40 different places for the house, select best one
            for number in range(total - 1):
                self.highest_score = 0

                #check which house needs to be placed
                if number_maison > 0:
                    house_type = 3
                    number_maison -=  1
                elif number_bungalow > 0:
                    house_type = 2
                    number_bungalow -= 1
                elif number_eengezinswoning > 0:
                    house_type = 1
                    number_eengezinswoning -= 1
            
                # creates house object at an arbitrary location outside the map
                house = self.amstelhaege.place_house(house_type, -100, -100)

                tries = 0
                while tries < 400:
                    placed = False
                    house.move(-100, -100)
                    
                    # generate random coordinates
                    while placed == False:
                        x = randrange(self.amstelhaege.width)
                        y = randrange(self.amstelhaege.length)

                        # check if the coordinates are available
                        if self.amstelhaege.check_location(x, y, house.width, house.length, house.free_area):
                            house.move(x,y)
                            placed = True
                        
                    # calculates worth og the map      
                    self.amstelhaege.get_free_space()
                    self.amstelhaege.calculate_worth()
                    self.score = self.amstelhaege.price
                    
                    # if score is higher than the currrent, save the position
                    if self.score > self.highest_score:
                        x_max = house.x_left
                        y_max = house.y_bottom
                        self.amstelhaege.get_free_space()
                        self.highest_score = self.score
                        
                    tries += 1

                # places the hous in the best position
                house.move(x_max, y_max)
                self.amstelhaege.get_free_space()
                self.amstelhaege.calculate_worth()

            return self.amstelhaege

    