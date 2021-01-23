from code.algorithms.simulated_annealing import Simulated_annealing

class Hillclimber:
    """
    Hillclimber class from which all the hillclimber algorithms inherit
    """
    def __init__(self, amstelhaege, sim_ann):
        self.amstelhaege = amstelhaege

        # if the user chose with simulated annealing, initialize
        if sim_ann:
            self.simulated_annealing = Simulated_annealing()
            self.condition = lambda: self.simulated_annealing.update_temperature()
            self.price_check = lambda a: self.simulated_annealing.check_price(a)

        else:
            self.iterations = 1000
            self.condition = lambda: self.get_condition()
            self.price_check = lambda a: self.check_price(a)
  
    def get_price(self):
        """
        Returns the price of Amstelhaege
        """
        self.amstelhaege.get_free_space()
        self.amstelhaege.calculate_worth()
        return self.amstelhaege.price

    
    def price_diff(self, old_price):
        """
        returns the price difference
        """

        self.amstelhaege.get_free_space()
        self.amstelhaege.calculate_worth()

        return self.amstelhaege.price - old_price
    
    def check_price(self, price_diff):
        """
        returns True when the old price was higher, else False
        """
        
        if price_diff < 0:
            return True
        return False

    def get_condition(self):
        """
        simple for loop implementation
        """
        
        if self.iterations == 0:
            return False

        self.iterations -= 1
        
        return True