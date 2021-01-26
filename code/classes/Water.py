class Water():
    """
    class which represents the water on the map
    """

    def __init__(self, name, x_bottom_left, y_bottom_left, x_top_right, y_top_right, width, length):
        self.name = name
        self.x_left = x_bottom_left
        self.y_bottom = y_bottom_left
        self.x_right = x_top_right
        self.y_top = y_top_right
        self.width = width
        self.length = length
     
        

