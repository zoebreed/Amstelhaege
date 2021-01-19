from random import randrange
from code.classes.Amstelhaege import Amstelhaege
    
class Random:
    """
    Class which executes the random algorithm.
    The houses are just randomly placed.
    """
    def __init__(self, amstelhaege):
        self.amstelhaege = amstelhaege

    def place_random(self, house_type, house_info):
        """
        places a house at a random valid position
        """
        while True:
            x = randrange(self.amstelhaege.width)
            y = randrange(self.amstelhaege.length)

            if self.amstelhaege.check_location(x, y, house_info[0], house_info[1], house_info[2]):
                self.amstelhaege.place_house(house_type, x, y)
                return


    def run(self):
        # iterates through the house types
        for house_type in self.amstelhaege.house_types:

            house_info = self.amstelhaege.house_types[house_type]

            # places the right amount of houses per house type
            for i in range(house_info[3]):
                
                # place the house at a random position
                self.place_random(house_type, house_info)

        self.amstelhaege.get_free_space()
        self.amstelhaege.calculate_worth()