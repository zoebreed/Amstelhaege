from random import randrange, choice
from code.algorithms.hillclimber import Hillclimber

class Hillclimber1(Hillclimber):
    """
    Executes the first version of the hillclimber algorithm. As input
    it takes amstelhaege with the houses already placed. Then a random 
    house is placed at a random location. If this random location 
    increases the total price, it stays. If this random location
    decreases the total price, we remove it.
    """

    def __init__(self, amstelhaege, sim_ann=False):
        Hillclimber.__init__(self, amstelhaege, sim_ann)

    def move_house_random(self, house):
        """
        Runs until available coordinates are found randomly and the house is places
        """
        while True:
            x = randrange(self.amstelhaege.width)
            y = randrange(self.amstelhaege.length)

            # check if the random coordinates are available
            if self.amstelhaege.check_location(x, y, house.width, house.length, house.free_area):
                house.move(x,y)
                return

    def run(self):
        """
        Runs the hillclimber algorith with the user chosen settings
        :return: The amstelhaege object with the improved house placement
        """
        
        while self.condition():
            
            old_price = self.amstelhaege.price
            
            # get a random house
            house = choice(self.amstelhaege.houses)

            # save the original coordinates for later
            x, y = house.x_left, house.y_bottom

            # move the house temporarily outside of the map to prevent overlap on itself
            house.move(-100, -100)

            # move the house to a random location within the map
            self.move_house_random(house)

            # get the difference between the old and new price
            price_diff = self.price_diff(old_price)

            # accept the change if the price is higher, else change back the coordinates
            if self.price_check(price_diff):

                house.move(x, y)
                self.amstelhaege.get_free_space()
                self.amstelhaege.calculate_worth()

        return self.amstelhaege