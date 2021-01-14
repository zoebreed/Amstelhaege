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
        self.house_list = []
        self.highest_score = None
        self.score = None    

    def run(self):
        total = self.amstelhaege.total
        # timeout_start = time.time()
        # while time.time() < timeout_start + timeout:
        
        # calculate number of houses for each house type to be placed
        number_eengezinswoning = self.amstelhaege.fraction_house_1 * total
        number_bungalow = self.amstelhaege.fraction_house_2 * total
        number_maison = ((self.amstelhaege.fraction_house_3 * total) - 1)

        # randomly places first house, which is maison
        x = randrange(self.amstelhaege.width)
        y = randrange(self.amstelhaege.length)
        first_house = House(x, y, 3)
        first_house.total_freearea = 10
        self.amstelhaege.houses.append(first_house)
        
        #calculate the worth of map
        self.amstelhaege.calculate_worth()
        self.highest_score = self.amstelhaege.price
            
        # consider 40 different places for next house, select best one
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
            
            # creates house object
            house = House(x, y, house_type)
            self.amstelhaege.houses.append(house)

            tries = 0
            while tries < 3:
                placed = False
                # generate coordinates
                while placed == False:
                    house.x_left = x
                    house.y_left = y
                    x = randrange(self.amstelhaege.width)
                    y = randrange(self.amstelhaege.length)

                    # check if the random coordinates are available
                    if self.amstelhaege.check_location(x, y, house.width, house.length, house.free_area):
                        house.move(x, y)
                        print(f"goed {house.x_left}")
                        placed = True
                    
                # calculates new worth        
                self.amstelhaege.get_free_space()
                self.amstelhaege.calculate_worth()
                self.score = self.amstelhaege.price
                
                # if score is higher than the currrent, save the position
                if self.score > self.highest_score:
                    print(f"hoogste: {house.x_left}")
                    self.highest_score = self.score
                    self.amstelhaege.price = self.highest_score

                tries += 1
        return self.amstelhaege

    