from code.algorithms.water_random import WaterRandom
from code.classes.Water import Water
from code.parameters import house1, house2, house3
from .House import House
from random import randrange
import csv

class Amstelhaege:
    """
    class which represents the area in which houses must be build 
    """
    def __init__(self, choice, n_houses):
        self.width = 180
        self.length = 160
        self.price = None

        self.total = n_houses
        self.house1_amount = int(house1.percentage * self.total)
        self.house2_amount = int(house2.percentage * self.total)
        self.house3_amount = int(house3.percentage * self.total)

        # information about each house type is stored here
        self.house = {1: house1, 2: house2, 3: house3}

        self.houses = []
        self.waters = []
             
        if choice == "random water":
            water = WaterRandom()
            self.waters = water.run()
        elif choice != 'greedy water':
            self.load_water(choice)
        
    def load_water(self, choice):
        """
        Loads the coordinates of the water from the csv file
        :param choice: 
        """        
        csv_file = [("data/wijk_1.csv"), ("data/wijk_2.csv"), ("data/wijk_3.csv")][choice]
    
        # retrieves the coordinates of the water
        with open(csv_file, 'r') as in_file:
            reader = csv.DictReader(in_file)
            for row in reader:
                bottom_x, bottom_y = row['bottom_left_xy'].split(",")
                top_x, top_y = row['top_right_xy'].split(",")
                x_bottom_left, y_bottom_left = int(bottom_x), int(bottom_y)
                x_top_right, y_top_right = int(top_x), int(top_y)
                width = x_top_right - x_bottom_left
                length = y_top_right - y_bottom_left

                # makes a Water object and appends it to the neighbourhood
                water = Water('water', x_bottom_left, y_bottom_left, x_top_right, y_top_right, width, length)
                self.waters.append(water)

    def load_water2(self, water_bodies):
        """
        loads the water coordinates from a generated list
        """
        for water in water_bodies:
            water_body = Water('water', water[0], water[2], water[1], water[3], water[1]-water[0], water[3]-water[2])
            self.waters.append(water_body)    

    def place_house(self, house_type, x, y):
        """
        places a new house and saves the created object
        """
        new_house = House(x, y, self.house[house_type])
        self.houses.append(new_house)
        return new_house

    def check_location(self, x, y, house):
        """
        checks whether a house can be placed at particular coordinates.
        :param x,y: coordinates of the location to check
        :param house: class or namedtuple where house info can be accesed
        """
        width, length = house.width, house.length
        extra = house.free_area

        # check if the house is placed in water
        for water in self.waters:
            if ( 
                x < water.x_right and
                (x + width) > water.x_left and
                y < water.y_top and
                (y + length) > water.y_bottom
               ):
               return False

        # check if the house is placed outside the map
        if (
            (x - extra) < 0 or
            (x + width + extra) > self.width or
            (y - extra) < 0 or 
            (y + length + extra) > self.length
            ):
            return False

        if len(self.houses) == 0:
            return True

        # check whether there is overlap with an existing house
        for house in self.houses:

            # get the biggest required free area
            if house.free_area > extra:
                extra = house.free_area

            if ( 
                x < (house.x_right + extra) and
                (x + width) > (house.x_left - extra) and
                y < (house.y_top + extra) and
                (y + length) > (house.y_bottom - extra)
               ):   
               return False
        return True
    
    def get_distance(self, house1, house2):
        """
        calculates the shortest distance between two houses
        """
        # calculate the horizontal distance
        if house1.x_right <= house2.x_left:
            horizontal = house2.x_left - house1.x_right
        else:
            horizontal = house1.x_left - house2.x_right

        # calculate the vertical distance
        if house1.y_top <= house2.y_bottom:
            vertical = house2.y_bottom - house1.y_top
        else:
            vertical = house1.y_bottom - house2.y_top

        # check if there is overlap
        if house1.x_left < house2.x_right and house1.x_right > house2.x_left:
            return vertical
        if house1.y_bottom < house2.y_top and house1.y_top > house2.y_bottom:
            return horizontal

        distance = max([horizontal, vertical])
        return distance

    def get_free_space(self):
        """
        assigns the free space
        """ 
        # if there is only 1 house return an arbitrary random number
        if len(self.houses) == 1:
            self.houses[0].total_freearea = randrange(20)
            return

        for house in self.houses:
            min_distance = 1000
            
            for house_check in self.houses:
                if house == house_check:
                    continue
            
                distance = self.get_distance(house, house_check)

                if distance < min_distance:
                    min_distance = distance
    
            house.total_freearea = min_distance

    def calculate_price(self):
        """
        function that calculates the price of the entire neighbourhood
        :return: The price of Amstelhaege (float)
        """
        price = 0
        self.get_free_space()
        for house in self.houses:
            # calculates the new price of the house 
            house.price = house.value * (1 + house.increase_value * (house.total_freearea - house.free_area))

            # add price to neighbourhood price
            price += house.price
        
        self.price = price
        return self.price
