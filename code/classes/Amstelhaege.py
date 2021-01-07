# import .house import House
import csv

from code.classes.Water import Water

class Amstelhaege():
    """
    class which represents the area in which houses must be build 
    """
    def __init__(self):
        self.neighbourhood = []
        self.length = 160
        self.width = 180

        self.fraction_house_1 = 0.6
        self.fraction_house_2 = 0.25
        self.fraction_house_3 = 0.15
        

    def load_water(self):
        """
        Loads the coordinates of the water from the csv file
        """
        # TODO je gebruikt nu maar 1 csv file
        csv_file = ("data/wijk_1.csv")
    
        # retrieves the coordinates of the water
        with open(csv_file, 'r') as in_file:
            reader = csv.DictReader(in_file)
            for row in reader:
                bottom_x, bottom_y = row['bottom_left_xy'].split(",")
                top_x, top_y = row ['bottom_right_xy'].split(",")

                id = row
                x_bottom_left, y_bottom_left = int(bottom_x), int(bottom_y)
                x_top_right, y_top_right = int(top_x), int(top_y)
                width = (water.x_top_right - water.x_bottom_left)
                height = (water.y_top_right - water.y_bottom_left)
                print(height)

                # makes a Water object and appends it to the neighbourhood
                water = Water('Water', id, x_bottom_left, y_bottom_left, x_top_right, y_top_right, width, height)
                self.neighbourhood.append(water)

        return neighbourhood


    def place_house(self):
        """
        places a new house and saves the created object
        """
        new_house = House(house_type, coordinates, extra_freearea)
        self.houses.append(new_house)
