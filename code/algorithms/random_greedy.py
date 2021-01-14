from code.classes.Amstelhaege import House
from random import randrange
from copy import deepcopy
from code.classes.Amstelhaege import Amstelhaege
from code.helpers.price import calculate_price

class Random_greedy():
    def __init__(self, choice, n_houses, amstelhaege):
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
        x = randrange(self.amstelhaege.length)
        y = randrange(self.amstelhaege.width)
        # house.update_worth()

        # check if the random coordinates are available
        if self.amstelhaege.check_location(x, y, house.length, house.width, house.free_area):
            # house.move(x,y)
            placed = True
    
 

    def run(self, choice, n_houses, amstelhaege):
        """
        function that tries to place the house in random places and places it on the
        best position for the specific house
        """
        highest_score, old_price = 0, 0
        total = n_houses


        #place water 
        amstelhaege = Amstelhaege(choice, n_houses)

        # calculate number of houses for each house type
        numb_eengezinswoning = amstelhaege.fraction_house_1 * total
        numb_bungalow = amstelhaege.fraction_house_2 * total
        numb_maison = amstelhaege.fraction_house_3 * total

        # randomly places first house, which is maison
        x = randrange(amstelhaege.length)
        y = randrange(amstelhaege.width)
        house_type = 3
        new_house = House(x, y, house_type)
        new_house.total_freearea = 2
        amstelhaege.houses.append(new_house)

        numb_maison = numb_maison + 1

        amstelhaege.calculate_worth()
        score = amstelhaege.price
        print(score)

        self.temp_house_list = amstelhaege.houses 

        
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
            
            amstelhaege.houses.append(temp_house)
         
            
            #TODO: wil je deze tries zelf kunnen bepalen?
            tries = 0
            while tries < 2:
                placed = False

                # generate coordinates
                while placed == False:
                    self.move_house_random(temp_house)
                
               
                self.get_free_space()
                price = calculate_price(amstelhaege.houses)
               
                if price > score:
                    score = price
                    self.temp_house_list = amstelhaege.house

                # return False
                    
                # # selects best place for the house
                # if self.check_price(old_price):
                #     highest_score = old_price
                #     best_x = x
                #     best_y = y
                
                tries += 1

        self.temp_house_list = amstelhaege.house      

        return amstelhaege, highest_score

    