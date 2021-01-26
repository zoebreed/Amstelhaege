import itertools 
from code.parameters import house1, house2, house3

class House():
    """
    class which represents a house 
    """
    id_iter = itertools.count()

    def __init__(self, x_bottom_left, y_bottom_left, house_type):
        self.house_type = house_type
        self.x_left = x_bottom_left
        self.y_bottom = y_bottom_left
        self.total_freearea = None
        self.minimum_distance = None
        self.price = None
        self.id = next(House.id_iter)
        self.worth = None
        
        # get the properties of the house depending on the type
        house = eval('house' + str(house_type))
        
        self.name = house.name
        self.length = house.length
        self.width = house.width
        self.increase_value = house.increase_value
        self.value = house.value
        self.free_area = house.free_area

        self.x_right = self.x_left + self.width
        self.y_top = self.y_bottom + self.length

    
    def move(self, x, y):
        """
        move the left bottom corner of the house to the (x,y) posistion
        """
        self.x_left = x
        self.x_right = x + self.width

        self.y_bottom = y
        self.y_top = y + self.length