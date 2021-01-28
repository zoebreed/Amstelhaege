from code.parameters import house1, house2, house3
import itertools 

class House():
    """
    class which represents a house 
    """
    id_iter = itertools.count()

    def __init__(self, x_left, y_bottom, house):
        self.x_left = x_left
        self.y_bottom = y_bottom
        self.id = next(House.id_iter)
        self.total_freearea = None
        self.minimum_distance = None
        self.price = None
        
        # initialize the properties of the house    
        self.house_type = house.house_type    
        self.name = house.name
        self.length = house.length
        self.width = house.width
        self.increase_value = house.increase_value
        self.value = house.value
        self.free_area = house.free_area

        self.x_right = self.x_left + self.width
        self.y_top = self.y_bottom + self.length

    
    def move(self, x=-100, y=-100):
        """
        move the left bottom corner of the house to the (x,y) posistion
        :param x, y: Default = (-100, -100)
        """
        self.x_left = x
        self.x_right = x + self.width

        self.y_bottom = y
        self.y_top = y + self.length