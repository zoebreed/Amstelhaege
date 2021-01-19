from random import randrange
from math import floor, ceil, sqrt
from code.classes.Water import Water
from random import randrange, uniform
# from code.classes.Amstelhaege import Amstelhaege

class randomWater:
    """
    places the bodies of water in a random position
    """
    def __init__(self, amstelhaege):
        self.amstelhaege = amstelhaege
        self.bodies = randrange(1, 5)
        self.total_area = 5760

    def check_water(self, x, y, width, length):
        for water in self.waters:
            if ( 
                x < (water.x_right) and
                (x + width) > (water.x_left) and
                y < (water.y_top) and
                (y + length) > (water.y_bottom)
               ):   
               return False
        return True

    def run(self):
        percentages = self.divide_percentage(self.bodies)
     
        index_water = 0
        while index_water < self.bodies:
            water_area = percentages[index_water] * self.total_area

            # dimension of water
            min_width = max(1, int(sqrt(5760 * (1 / 4))))
            max_width = int(sqrt(water_area * (4/ 1)))
            water_width = int(randrange(min_width, max_width))
            water_length= int(ceil(water_area / water_width))
            
            # generate random coordinates
            x = randrange(0, int(self.amstelhaege.width - water_width))
            y = randrange(0, int(self.amstelhaege.length - water_length))
            x_top_right = x + water_width
            y_top_right = y + water_length

            # checks if the position is valid and places it on the map
            if self.check_water(x, y, water_width, water_length):
                water = Water('water', index_water, x, y, x_top_right, y_top_right, water_width, water_length)
                self.amstelhaege.waters.append(water)
                index_water += 1
    
    def divide_percentage(self,bodies, percentage_list=[1]):
        if bodies == 1:
            return percentage_list
      
        # divide biggest part
        list.sort(percentage_list)
        part = percentage_list[-1]

        # remove the part we are going to split in two
        percentage_list = percentage_list[:-1]

        # split the biggest part into two smaller parts
        part1 = uniform(0, part)
        part2 = part - part1

        # add the new part to the list
        percentage_list.append(part1)
        percentage_list.append(part2)

        #recursion
        return self.divide_percentage(bodies-1, percentage_list)
