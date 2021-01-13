from code.algorithms.random_placement import random_placement
from code.algorithms.hillclimber1 import Hillclimber_1
from copy import deepcopy

def repeat(amstelhaege, iterations, algorithm):
    """
    repeats the given algorithm n times and gets the best result
    """
    highest_score = 0

    for i in range(iterations):

        amstelhaege_copy = deepcopy(amstelhaege)

        # run the chosen algorithm
        if algorithm == 'random':
            amstelhaege = random_placement(amstelhaege_copy)

        elif algorithm == 'hillclimber':
            hillclimber1 = Hillclimber_1(amstelhaege_copy)
            amstelhaege = hillclimber1.run(10)

        new_score = amstelhaege.price

        # check if the new price is higher and if so, save the map
        if new_score > highest_score:
            best_map = deepcopy(amstelhaege)
            highest_score = new_score
    
    return best_map, highest_score