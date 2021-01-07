# import .house import House
import csv

from code.classes.Water import Water

class Amstelhaege():
    """
    class which represents the area in which houses must be build 
    """
    def __init__(self):
        # self.neighbourhood = []
        self.length = 180
        self.width = 160

        self.fraction_house_1 = 0.6
        self.fraction_house_2 = 0.25
        self.fraction_house_3 = 0.15
        

    def load_water(choice):
        """
        Loads the coordinates of the water from the csv file
        """
        # TODO  deze lijst wil je niet hier aanmaken
        neighbourhood = []
        # TODO je gebruikt nu maar 1 csv file
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


    def place_house(self):
        """
        places a new house and saves the created object
        """
        new_house = House(house_type, coordinates, extra_freearea)
        self.houses.append(new_house)
