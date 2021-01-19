import math
from random import randint

class Water():
    """
    class which represents the water on the map
    """

    def __init__(self, name, id, x_bottom_left, y_bottom_left, x_top_right, y_top_right, width, length):
        self.max_water = 4
        self.min_water = 1
        self.min_ratio = 1
        self.max_ratio = 4 
        self.water_area = 5760
        self.nr_water = 3
        
        self.name = name
        self.id = id
        self.x_left = x_bottom_left
        self.y_bottom = y_bottom_left
        self.x_right = x_top_right
        self.y_top = y_top_right
        self.width = width
        self.length = length
        self.square_area = self.width * self.length
        self.square_area_oval = (math.pi * (self.width/2) * (self.length/2))
        
        # (int(randrange(self.min_water, self.max_water)))
    

