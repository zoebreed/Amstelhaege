from random import random, randrange
from math import floor, ceil, sqrt
# from code.classes.Water import Water
# from code.classes.Amstelhaege import Amstelhaege

class randomWater:
    """
    places the bodies of water in a random position
    """
    def __init__(self, amstelhaege):
        self.amstelhaege = amstelhaege
        self.bodies = randrange(0, 5)
        self.total_area = 5760

        # self.max_length = 
        # self.water_length = randrange(4, 150)
        # self.water_width = randrange(int(ceil(water_area / water_length)), water_length

    # hoogte breedte verhouding moet tussen 1:1 en 1:4 liggen
    def run(self):
        index_water = 0
        while index_water < water.nr_water:
            water_area = perecentages[index_water] * water.water_area

            # dimension of water
            min_width = max(1, int(sqrt(water_area * water.max_ratio / water.min_ratio)))
            max_width = int(sqr(water_area * water.max_ratio / water.min_ratio))
            water_width = random.randint(min_length, max_length)
            water_length= int(ceil(water_area / water_length))

            # generate random coordinates
            x = random.randint(0, amstelhaege.width - water_width)
            y = random.randint(0, int(amstelhaege.length - water_length))
            x_top_right = x + water_width
            y_top_right = y + water_length

            # check of de positie valid is
            if amstelhaege.check_location:
                index_water += 1
            
            # plaats het water
            water = Water('water', index_water, x, y, x_top_right, y_top_right, water_width, water_length)
            amstelhaege.waters.append(water)
            print(amstelhaege.waters)
            
        # for i in range(self.bodies - 1):
        #     area = floor(self.remaining_area/randrange(self.remaining_area/4))
        #     self.remaining_area -= area
        #     areas.append(area)
        # area.append(self.remaining_area)

        # ab + cd + ef + gh = 5760
        # where minimally 1:4
