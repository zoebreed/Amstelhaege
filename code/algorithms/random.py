from code.parameters import house1, house2, house3
from random import randrange

class Random:
    """
    Class which executes the random algorithm.
    Places the houses at randomly generated coordinates.
    """
    def __init__(self, amstelhaege):
        self.amstelhaege = amstelhaege

    def place_random(self, house):
        """
        places a house at a random valid position
        """
        while True:
            x = randrange(self.amstelhaege.width)
            y = randrange(self.amstelhaege.length)

            if self.amstelhaege.check_location(x, y, house):
                self.amstelhaege.place_house(house.type, x, y)
                return

    def run(self):
        # iterates through the house types
        for house in self.amstelhaege.house.values():

            # places the right amount of houses per house type
            for i in range(int(house.percentage * self.amstelhaege.total)):
                
                # place the house at a random position
                self.place_random(house)

        self.amstelhaege.calculate_price()