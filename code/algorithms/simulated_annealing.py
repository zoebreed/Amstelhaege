from math import exp
from random import random


class Simulated_annealing():
    """
    class which is used for the simulated annealing algorithm.
    It is used inside other algorithms. initialize the class in 
    the beginning of the algorithm and call run when checking the
    price difference 
    """
    def __init__(self):
        self.Tmax = 170000
        self.Tmin = 1000
        self.alpha = 10
        self.T = self.Tmax

    def update_temperature(self):
        """
        lowers the temperature each iteration and checks whether
        the minimum temperature has been reached
        """

        if self.T < self.Tmin:
            return False
        self.T -= self.alpha

        return True
        
    def check_price(self, price_diff):
        """
        If the price difference is positive, accept the change.
        Else, use chance to sometimes accept a negative change.
        """
        chance = exp(price_diff / self.T)

        if price_diff < 0 and not chance > random():
            return True
        
        return False