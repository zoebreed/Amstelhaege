from .House import House
import csv

from code.classes.Water import Water

class Amstelhaege():
    """
    class which represents the area in which houses must be build 
    """
    def __init__(self, choice):
        # self.neighbourhood = []
        self.length = 180
        self.width = 160

        self.fraction_house_1 = 0.6
        self.fraction_house_2 = 0.25
        self.fraction_house_3 = 0.15
        self.total = 60

        self.houses = []
        self.waters = self.load_water(choice)
        

    def load_water(self, choice):
        """
        Loads the coordinates of the water from the csv file
        """
        # TODO  deze lijst wil je niet hier aanmaken
        neighbourhood = []
       
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
                water = Water('Water', id, x_bottom_left, y_bottom_left, x_top_right, y_top_right, width, height)
                neighbourhood.append(water)

        return neighbourhood


    def place_house(self, house_type, x, y):
        """
        places a new house and saves the created object
        """
        new_house = House(x, y, house_type, 0)
        self.houses.append(new_house)

    
    def check_location(self, x, y, length, width, extra):
        """
        checks whether a house can be placed at particular coordinates.
        x and y are the center location of the house
        """
        if len(self.houses) == 0:
            return True

        # check whether there is overlap with an existing house
        for house in self.houses:
            if ( 
                (x - extra) < (house.x_top_right + house.free_area) and
                (x + width + extra) > (house.x_bottom_left - house.free_area) and
                (y - extra) < (house.y_top_right + house.free_area) and
                (y + length + extra) > (house.y_bottom_left - house.free_area)
               ):
               return False

        for water in self.waters:
            if ( 
                (x) < water.x_top_right and
                (x + width) > water.x_bottom_left and
                (y) < water.y_top_right and
                (y + length) > water.y_bottom_left
               ):
               return False


        return True