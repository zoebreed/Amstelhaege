import math

class Water():
    """
    class which represents the water on the map
    """

    def __init__(self, name, id, x_bottom_left, y_bottom_left, x_top_right, y_top_right, width, height):

        self.name = name
        self.id = id
        self.x_left = x_bottom_left
        self.y_bottom = y_bottom_left
        self.x_right = x_top_right
        self.y_top = y_top_right
        self.width = width
        self.height = height
        self.square_area = self.width * self.height
        self.square_area_oval = (math.pi * (self.width/2) * (self.height/2))
    
    def load_water(self, choice):
        """
        Loads the coordinates of the water from the csv file
        """

        if choice == "random":
            water = random_water(self)
            water.run()
            return
        
        csv_file = [("data/wijk_1.csv"), ("data/wijk_2.csv"), ("data/wijk_3.csv"), x()][choice]
    
        # retrieves the coordinates of the water
        with open(csv_file, 'r') as in_file:
            reader = csv.DictReader(in_file)
            for row in reader:
                bottom_x, bottom_y = row['bottom_left_xy'].split(",")
                top_x, top_y = row ['top_right_xy'].split(",")

                id = row
                x_bottom_left, y_bottom_left = int(bottom_x), int(bottom_y)
                x_top_right, y_top_right = int(top_x), int(top_y)
                width = (x_top_right - x_bottom_left)
                height = (y_top_right - y_bottom_left)

                # makes a Water object and appends it to the neighbourhood
                water = Water('water', id, x_bottom_left, y_bottom_left, x_top_right, y_top_right, width, height)
                self.waters.append(water)

    

