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
    function that tries to place the house in random places and places it on the
    best position for the specific house
    """

    def __init__(self, amstelhaege):
        self.amstelhaege = deepcopy(amstelhaege)
        self.temp_house_list = []
        self.highest_score = None
        self.score = None    

    def run(self, timeout):
        total = self.amstelhaege.total
        timeout_start = time.time()

        while time.time() < timeout_start + timeout:
            
            # calculate number of houses for each house type to be placed
            numb_eengezinswoning = self.amstelhaege.fraction_house_1 * total
            numb_bungalow = self.amstelhaege.fraction_house_2 * total
            numb_maison = ((self.amstelhaege.fraction_house_3 * total) - 1)

            # randomly places first house, which is maison
            x = randrange(self.amstelhaege.width)
            y = randrange(self.amstelhaege.length)
            first_house = House(x, y, 3)
            first_house.total_freearea = randrange(self.amstelhaege.length)
            self.amstelhaege.houses.append(first_house)
            self.temp_house_list = self.amstelhaege.houses
            
            #calculate the worth of map
            self.amstelhaege.calculate_worth()
            self.highest_score = self.amstelhaege.price
             
            # consider 40 different places for next house, select best one
            for number in range(total - 1):
                #check which house needs to be placed
                if numb_maison > 0:
                    house_type = 3
                    numb_maison -=  1
                elif numb_bungalow > 0:
                    house_type = 2
                    numb_bungalow -= 1
                elif numb_eengezinswoning > 0:
                    house_type = 1
                    numb_eengezinswoning -= 1
                
                # creates house object
                temp_house = House(x, y, house_type)
                self.amstelhaege.houses.append(temp_house)

                tries = 0
                while tries < 2:
                    placed = False
                
                    # generate coordinates
                    while placed == False:
                        temp_house.x_left = x
                        temp_house.y_left = y
                        x = randrange(self.amstelhaege.width)
                        y = randrange(self.amstelhaege.length)
                        
                    
                        self.amstelhaege.get_free_space()

                        # update de waarde van 1 huis, dus dan kunnen we de totale waarde
                        # bereken met het bij elkaar optellen van de huizen waarde.
                        temp_house.update_worth()

                        # check if the random coordinates are available
                        if self.amstelhaege.check_location(x, y, temp_house.width, temp_house.length, temp_house.free_area):
                            placed = True
                       
                    # calculates new worth        
                    self.amstelhaege.calculate_worth()
                    self.score = self.amstelhaege.price
                    
                    # if score is higher than the currrent, save the position
                    if self.score > self.highest_score:
                        self.highest_score = self.score
                        print(self.highest_score)
                        self.temp_house_list = self.amstelhaege.houses

                    tries += 1
                house = House(x, y, house_type)

            self.temp_house_list = self.amstelhaege.houses      
            
        return self.amstelhaege, self.highest_score

    