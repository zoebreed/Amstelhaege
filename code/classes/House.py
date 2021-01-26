import itertools 

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
        if self.house_type == 1:
            self.name = 'eengezinswoning'
            #self.id = id
            self.length = 8
            self.width = 8
            self.increase_value = 0.03
            self.value = 285000
            self.free_area = 2
        elif self.house_type == 2:
            self.name = 'bungalow'
            #self.id = id
            self.length = 7
            self.width = 11
            self.increase_value = 0.04
            self.value = 399000
            self.free_area = 3
        elif self.house_type == 3:
            self.name = 'maison'
            #self.id = id
            self.length = 10
            self.width = 12
            self.increase_value = 0.06
            self.value = 610000
            self.free_area = 6

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

  

