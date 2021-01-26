from code.algorithms.simulated_annealing import SimulatedAnnealing
from code.parameters import iters

class Hillclimber:
    """
    Hillclimber class from which all the hillclimber algorithms inherit
    :param amstelhaege: The object amstelhaege
    :param sim_ann: Whether to use simulated annealing or not, True or False
    """
    
    def __init__(self, amstelhaege, sim_ann):
        self.amstelhaege = amstelhaege

        # if the user chose simulated annealing, initialize
        if sim_ann:
            self.simulated_annealing = SimulatedAnnealing()
            self.condition = lambda: self.simulated_annealing.update_temperature()
            self.price_check = lambda a: self.simulated_annealing.check_price(a)
        else:
            self.iterations = iters.hillclimber
            self.condition = lambda: self.get_condition()
            self.price_check = lambda a: self.check_price(a)
     
    def price_diff(self, old_price):
        """
        :param: The old price of amstelhaege
        :return: The price difference between the current amstelhaege and the old price (float)
        """
        self.amstelhaege.get_price()
        return self.amstelhaege.price - old_price
    
    def check_price(self, price_diff):
        """
        :param: The price difference between the old and new amstelhaege, new - old
        :return: True when the old price was higher, else False
        """
        if price_diff < 0:
            return True
        return False

    def get_condition(self):
        """
        simple for loop implementation
        :return: False when the for loop ended, else True
        """
        if self.iterations == 0:
            return False

        self.iterations -= 1
        return True