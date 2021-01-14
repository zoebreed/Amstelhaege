from code.algorithms.random import random
from code.algorithms.hillclimber1 import Hillclimber_1
from code.algorithms.hillclimber2 import Hillclimber_2
from code.algorithms.random_greedy import Random_greedy
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
            amstelhaege_copy = random(amstelhaege_copy)
        
        elif algorithm == 'random_greedy':
            random_greedy = Random_greedy(amstelhaege_copy)
            amstelhaege_copy = random_greedy.run(10)

        elif algorithm == 'hillclimber':
            hillclimber1 = Hillclimber_1(amstelhaege_copy)
            amstelhaege_copy = hillclimber1.run_sa()

        elif algorithm == 'hillclimber2':
            hillclimber2 = Hillclimber_2(amstelhaege_copy)
            amstelhaege_copy = hillclimber2.run(30)

        new_score = amstelhaege_copy.price

        # check if the new price is higher and if so, save the map
        if new_score > highest_score:
            best_map = deepcopy(amstelhaege_copy)
            highest_score = new_score

        print(new_score)
    return best_map, highest_score