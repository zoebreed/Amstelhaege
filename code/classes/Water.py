class Water():
    """
     class which represents the water on the map
    """

    def __init__(self, name, id, x_bottom_left, y_bottom_left, x_top_right, y_top_right, width, height):
        self.name = name
        self.id = id
        self.x_bottom_left = x_bottom_left
        self.y_bottom_left = y_bottom_left
        self.x_top_right = x_top_right
        self.y_top_right = y_top_right
        self.width = width
        self.height = height