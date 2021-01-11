from .House import House
import csv

from code.classes.Water import Water
from code.helpers.price import calculate_price, minimum_distance
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
        self.total = n_houses

        self.houses = []
        self.waters = self.load_water(choice)
        

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
                self.neighbourhood.append(water)

        return self.neighbourhood


    def place_house(self, house_type, x, y):
        """
        places a new house and saves the created object
        x and y are the bottom left coordinates of the house
        """
        new_house = House(x, y, house_type)

        self.houses.append(new_house)
        self.neighbourhood.append(new_house)

        #calculates minimum distance and price
        if len(self.houses) == self.total:
            minimum_distance(self.neighbourhood)

            self.price = calculate_price(self.neighbourhood)
            return self.neighbourhood, self.price
 
    def check_location(self, x, y, length, width, extra):
        """
        checks whether a house can be placed at particular coordinates.
        x and y are the center location of the house
        """
        for water in self.waters:
            if ( 
                x < water.x_right and
                (x + length) > water.x_left and
                y < water.y_top and
                (y + width) > water.y_bottom
               ):
               return False

        if len(self.houses) == 0:
            return True

        # check whether there is overlap with an existing house
        for house in self.houses:
            if ( 
                (x - extra) < (house.x_right + house.free_area) and
                (x + length + extra) > (house.x_left - house.free_area) and
                (y - extra) < (house.y_top + house.free_area) and
                (y + width + extra) > (house.y_bottom - house.free_area)
               ):   
               return False

        return True
    
    def get_distance(self, house1, house2):
        """
        calculates the shortest distance between two houses
        """
        if house2.extra_freearea == None:
            free_space = 0
        else:
            free_space = house2.extra_freearea

        # calculate the horizontal distance
        if house1.x_right <= (house2.x_left - free_space):
            horizontal = house2.x_left - house1.x_right
        elif house1.x_left > (house2.x_right + free_space):
            horizontal = house1.x_left - house2.x_right

        # calculate the vertical distance
        if house1.y_top <= (house2.y_bottom + free_space):
            vertical = house2.y_bottom - house1.y_top
        elif house1.y_bottom > (house2.y_top - free_space):
            vertical = house1.y_bottom - house2.y_top

        # check if there is overlap
        if self.overlap_x(house1, house2, free_space):
            return vertical
        if self.overlap_y(house1, house2, free_space):
            return horizontal

        distance = max([horizontal, vertical])
        return distance

    def overlap_x(self, house1, house2, free_space):
        """
        Checks whether there is overlap in the x-direction
        """

        if house1.x_left <= (house2.x_right + free_space) and house1.x_right >= (house2.x_left - free_space):
            return True
        
        return False

    def overlap_y(self, house1, house2, free_space):
        """
        Checks whether there is overlap in the y-direction
        """

        if house1.y_bottom <= (house2.y_top + free_space) and house1.y_top >= (house2.y_bottom - free_space):
            return True

        return False



    def random_free_space(self):
        """
        assigns the free space randomly
        """
        
        for house in self.houses:
            
            min_distance = 1000

            for house_check in self.houses:

                if house == house_check:
                    continue

                distance = self.get_distance(house, house_check)

                if house_check.extra_freearea != None:
                    distance -= house_check.extra_freearea

                if distance < min_distance:
                    min_distance = distance
                    min_house = house_check
            if min_house.extra_freearea == None:
                house.extra_freearea = randrange(min_distance)

            else:

                house.extra_freearea = min_distance 


                