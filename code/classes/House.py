class House():
    """
     class which represents a house 
    """

    def __init__(self, x_bottom_left, y_bottom_left, x_top_right, y_top_right, house_type, extra_freearea):
        self.house_type = house_type
        self.x_bottom_left = x_bottom_left
        self.y_bottom_left = y_bottom_left
        self.x_top_right = x_top_right
        self.y_top_right = y_top_right
        self.extra_freearea = extra_freearea

        if self.house_type == 1:
            self.length = 8
            self.width = 8
            self.increase_value = 0.03
            self.value = 285000
            self.free_area = 2
        elif self.house_type == 2:
            self.length = 7
            self.width = 11
            self.increase_value = 0.04
            self.value = 399000
            self.free_area = 3
        elif self.house_type == 3:
            self.length = 10
            self.width = 12
            self.increase_value = 0.06
            self.value = 610000
            self.free_area = 6

    def check_border(self): 
        check = False
        # check corner 1 (bottom left)
        if self.x_bottom_left - self.free_area == 0 or self.y_bottom_left - self.free_area == 0:
            check = True
        
        # check corner 2 (bottom right)
        elif self.x_top_right + self.free_area == 180 or self.y_bottom_left - self.free_area == 0:
            check = True
        
        # check corner 3 (top right)
        elif self.x_top_right + self.free_area == 180 or self.y_top_right + self.free_area == 160:
            check = True

        # check corner 4 (top left)
        elif self.x_bottom_left - self.free_area == 0 or self.y_top_right + self.free_area == 160:
            check = True

        return check


