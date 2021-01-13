from .House import House
import csv

from code.classes.Water import Water
from code.helpers.price import calculate_price#, minimum_distance
from random import randrange


class Amstelhaege():
    """
    class which represents the area in which houses must be build 
    """
    def __init__(self, choice, n_houses):
        self.neighbourhood = []
        self.length = 180
        self.width = 160
        self.price = None


        self.fraction_house_1 = 0.6
        self.fraction_house_2 = 0.25
        self.fraction_house_3 = 0.15
        # self.fraction_house_1 = 0.2
        # self.fraction_house_2 = 0.2
        # self.fraction_house_3 = 0.6
        self.total = n_houses

        self.houses = []
        self.waters = []
        self.load_water(choice)
        

    def load_water(self, choice):
        """
        Loads the coordinates of the water from the csv file
        """
 
        csv_file = [("data/wijk_1.csv"), ("data/wijk_2.csv"), ("data/wijk_3.csv")][choice]
    
        # retrieves the coordinates of the water
        with open(csv_file, 'r') as in_file:
            reader = csv.DictReader(in_file)
            for row in reader:
                bottom_x, bottom_y = row['bottom_left_xy'].split(",")
                top_x, top_y = row ['top_right_xy'].split(",")

                id = row
                x_bottom_left, y_bottom_left = int(bottom_x), int(bottom_y)
                x_top_right, y_top_right = int(top_x), int(top_y)
                height = (x_top_right - x_bottom_left)
                width = (y_top_right - y_bottom_left)

                # makes a Water object and appends it to the neighbourhood
                water = Water('water', id, x_bottom_left, y_bottom_left, x_top_right, y_top_right, width, height)
                self.waters.append(water)
                self.neighbourhood.append(water)



    def place_house(self, house_type, x, y):
        """
        places a new house and saves the created object
        x and y are the bottom left coordinates of the house
        """
        new_house = House(x, y, house_type)

        self.houses.append(new_house)
        self.neighbourhood.append(new_house)

        # #calculates minimum distance and price
        # if len(self.houses) == self.total:
        #     minimum_distance(self.neighbourhood)

        #     self.price = calculate_price(self.neighbourhood)
        #     return self.neighbourhood, self.price
    
    def calculate_worth(self):
        #calculates minimum distance and price
        if len(self.houses) == self.total:
            #minimum_distance(self.neighbourhood)

            self.price = calculate_price(self.neighbourhood)
            return self.neighbourhood, self.price

    def check_location(self, x, y, length, width, extra):
        """
        checks whether a house can be placed at particular coordinates.
        x and y are the center location of the house
        """

        # check if the house is placed in water
        for water in self.waters:
            if ( 
                x < water.x_right and
                (x + length) > water.x_left and
                y < water.y_top and
                (y + width) > water.y_bottom
               ):
               return False

        # check if the house is placed outside the map
        if (
            (x - extra) < 0 or
            (x + length + extra) > self.width or
            (y - extra) < 0 or 
            (y + width + extra) > self.length
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
                (x + length) > (house.x_left - extra) and
                y < (house.y_top + extra) and
                (y + width) > (house.y_bottom - extra)
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
        elif house1.x_left >= house2.x_right:
            horizontal = house1.x_left - house2.x_right

        # calculate the vertical distance
        if house1.y_top <= house2.y_bottom:
            vertical = house2.y_bottom - house1.y_top
        elif house1.y_bottom >= house2.y_top:
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
        
        for house in self.houses:
            
            min_distance = 1000

            for house_check in self.houses:

                if house == house_check:
                    continue

                distance = self.get_distance(house, house_check)

                if distance < min_distance:
                    min_distance = distance
    
            house.total_freearea = min_distance