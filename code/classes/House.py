class House():
    """
    class which represents a house 
    """

    def __init__(self, x_bottom_left, y_bottom_left, house_type):
        self.house_type = house_type
        self.x_left = x_bottom_left
        self.y_bottom = y_bottom_left
        self.extra_freearea = None
        self.minimum_distance = None
        self.price = None
        self.id = id

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
            self.length = 11
            self.width = 7
            self.increase_value = 0.04
            self.value = 399000
            self.free_area = 3
        elif self.house_type == 3:
            self.name = 'maison'
            #self.id = id
            self.length = 12
            self.width = 10
            self.increase_value = 0.06
            self.value = 610000
            self.free_area = 6

        self.x_right = self.x_left + self.width
        self.y_top = self.y_bottom + self.width

    def check_border(self): 
        check = False
        # check corner 1 (bottom left)
        if self.x_left - self.free_area == 0 or self.y_bottom - self.free_area == 0:
            check = True
        
        # check corner 2 (bottom right)
        elif self.x_right + self.free_area == 160 or self.y_bottom - self.free_area == 0:
            check = True
        
        # check corner 3 (top right)
        elif self.x_right + self.free_area == 160 or self.y_top + self.free_area == 180:
            check = True

        # check corner 4 (top left)
        elif self.x_left - self.free_area == 0 or self.y_top + self.free_area == 180:
            check = True

        return check


