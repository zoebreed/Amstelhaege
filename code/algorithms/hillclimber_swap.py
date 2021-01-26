from random import choice
from code.algorithms.hillclimber import Hillclimber

class HillclimberSwap(Hillclimber):
    """
    Executes the swap version of the hillclimber algorithm. As input
    it takes amstelhaege with the houses already placed.
    Then a random house is swapped with another random house. If this 
    swap increases the total price, it stays. If this swap decreases
    the total price, we revert it.
    """

    def __init__(self, amstelhaege, sim_ann=False):
        Hillclimber.__init__(self, amstelhaege, sim_ann)

    def swap(self, house1, house2):
        """
        Swaps the location of house1 and house2 if possible
        :param house: house1 and house2 are objects
        :return: True when succesfull
        """
        # save the original coordinates for later
        x, y = house1.x_left, house1.y_bottom
        x2, y2 = house2.x_left, house2.y_bottom

        # move the house temporarily outside of the map to prevent overlap on itself
        house1.move()
        house2.move()

        if self.amstelhaege.check_location(x2, y2, house1) and self.amstelhaege.check_location(x, y, house2):
            house1.move(x2, y2)
            house2.move(x, y)
            return True
            
        house1.move(x, y)
        house2.move(x2, y2)
        return False

    def run(self):
        """
        Runs the hillclimber algorith with the chosen settings
        :return: The amstelhaege object with the improved house placement
        """
        while self.condition():
            old_price = self.amstelhaege.price
            
            # select two random houses
            house1 = choice(self.amstelhaege.houses)
            house2 = choice(self.amstelhaege.houses)
            
            # if they can't be swapped, go to the next looped
            if not self.swap(house1, house2):
                continue

            # get the difference between the old and new price
            price_diff = self.price_diff(old_price)

            # accept the change if the price is higher, else change back the coordinates
            if self.price_check(price_diff):
                self.swap(house1, house2)
                self.amstelhaege.get_price()

        return self.amstelhaege