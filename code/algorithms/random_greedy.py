from code.classes.Amstelhaege import House
from random import randrange
from copy import deepcopy
from code.classes.Amstelhaege import Amstelhaege
from code.helpers.price import calculate_price
import time

class Random_greedy():
    def __init__(self, amstelhaege):
        self.amstelhaege = deepcopy(amstelhaege)
        self.temp_house_list = []
    
    # def check_price(self):
    #     """
    #     returns True when the new price is higher, False otherwise
    #     """
    #     self.amstelhaege.get_free_space()
    #     self.amstelhaege.calculate_worth()

    #     if self.amstelhaege.price > old_price:
    #         return True
    #     return False
    
    def move_house_random(self, house):
        """
        runs until available coordinates are found randomly and the house is places
        """
        x = randrange(self.amstelhaege.width)
        y = randrange(self.amstelhaege.length)
        # house.update_worth()

        # check if the random coordinates are available
        if self.amstelhaege.check_location(x, y, house.width, house.length, house.free_area):
            house.move(x,y)
            placed = True
            print("is True")
 

    def run(self, timeout):
        """
        function that tries to place the house in random places and places it on the
        best position for the specific house
        """
        highest_score, old_price = 0, 0
        total = self.amstelhaege.total

        timeout_start = time.time()

        while time.time() < timeout_start + timeout:
            #place water 
            # amstelhaege = Amstelhaege(choice, n_houses)

            # calculate number of houses for each house type
            numb_eengezinswoning = self.amstelhaege.fraction_house_1 * total
            numb_bungalow = self.amstelhaege.fraction_house_2 * total
            numb_maison = self.amstelhaege.fraction_house_3 * total

            # randomly places first house, which is maison
            x = randrange(self.amstelhaege.width)
            y = randrange(self.amstelhaege.length)
            house_type = 3
            new_house = House(x, y, house_type)
            new_house.total_freearea = 2
            self.amstelhaege.houses.append(new_house)

            # updates number of houses
            numb_maison = numb_maison + 1

            #calculate the worth of map
            self.amstelhaege.calculate_worth()
            score = self.amstelhaege.price
        

            self.temp_house_list = self.amstelhaege.houses 

            
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
                
                temp_house = House(x, y, house_type)
                
                self.amstelhaege.houses.append(temp_house)
            
                
                #TODO: wil je deze tries zelf kunnen bepalen?
                tries = 0
                while tries < 2:
                    placed = False
                    print("placed is False")

                    # generate coordinates
                    while placed == False:
                        x = randrange(self.amstelhaege.width)
                        y = randrange(self.amstelhaege.length)

        
                        # check if the random coordinates are available
                        if self.amstelhaege.check_location(x, y, temp_house.width, temp_house.length, temp_house.free_area):
                            placed = True
                            print("placed is True")

                        # self.move_house_random(temp_house)
                    
                    # calculates new worth
                    print(self.amstelhaege.houses)
                    print(self.amstelhaege.houses.x_left)
                    self.amstelhaege.get_free_space()
                    
                    price = calculate_price(self.amstelhaege.houses)
                    
                    # selects best place for the house
                    if price > score:
                        score = price
                        best_x = x 
                        best_y = y
                        self.temp_house_list = self.amstelhaege.house

                    tries += 1
                house = House(best_x, best_y, house_type)

            self.temp_house_list = self.amstelhaege.house      

        return self.amstelhaege, highest_score

    