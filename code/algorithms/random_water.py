from random import randrange, randint, uniform
from math import ceil, sqrt
from code.classes.Water import Water

class randomWater:
    """
    places the bodies of water in a random position
    """
    def __init__(self):
        self.total_area = 5760
        self.min_ratio = 1
        self.max_ratio = 4
        self.new_waters = []

    def check_water(self, x, y, width, length):
        """
        function that checks if the water bodies overlap
        """
        for water in self.new_waters:
            if ( 
                x < (water.x_right) and
                (x + width) > (water.x_left) and
                y < (water.y_top) and
                (y + length) > (water.y_bottom)
               ):   
               return False
        return True

    def divide_percentage(self, bodies, percentage_list=[1]):
        """
        function that devides splits the number 1 (n - 1) times into two random parts
        """
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

        # add the new parts to the list
        percentage_list.extend([part1,part2])

        return self.divide_percentage((bodies - 1), percentage_list)
  
    def run(self):
        bodies = randint(self.min_ratio, self.max_ratio)
        percentages = self.divide_percentage(bodies)

        index_water = 0
        while index_water < bodies:
            water_area = percentages[index_water] * self.total_area

            # dimension of water
            min_width = max(1, int(sqrt(water_area * (self.min_ratio / self.max_ratio))))
            max_width = int(sqrt(water_area * (self.max_ratio / self.min_ratio)))
            water_width = int(randrange(min_width, max_width))
            water_length= int(ceil(water_area / water_width))
            
            # generate random coordinates
            x = randrange(0, int(180 - water_width))
            y = randrange(0, int(160- water_length))
            x_top_right = x + water_width
            y_top_right = y + water_length

            # checks if the position is valid and places it on the map
            if self.check_water(x, y, water_width, water_length):
                water = Water('water', index_water, x, y, x_top_right, y_top_right, water_width, water_length)
                self.new_waters.append(water)
                index_water += 1

        return self.new_waters
    

