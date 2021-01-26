from code.algorithms.hillclimber_random import HillclimberRandom
from code.algorithms.hillclimber_step import HillclimberStep
from code.algorithms.hillclimber_swap import HillclimberSwap
from code.algorithms.genetic import Genetic, Chromosome
from code.algorithms.random_greedy import RandomGreedy
from code.algorithms.random import Random
from copy import deepcopy

def repeat(amstelhaege, user):
    """
    repeats the given algorithm n times and gets the best result
    :return: highest map, highest price, average price
    """
    highest_score, total_score = 0, 0

    for i in range(user.iterations):
        amstelhaege_copy = deepcopy(amstelhaege)

        # place the houses using the chosen algorithm
        if user.algorithm_p == 'random':
            random = Random(amstelhaege_copy)
            random.run()
        elif user.algorithm_p == 'random greedy' and user.neighbourhood == 'greedy water':
            random_greedy = RandomGreedy(amstelhaege_copy, water=True)
            random_greedy.run()
        elif user.algorithm_p == 'random greedy':
            random_greedy = RandomGreedy(amstelhaege_copy)
            random_greedy.run()
        elif user.algorithm_p == 'greedy' and user.neighbourhood == 'greedy water':
            random_greedy = RandomGreedy(amstelhaege_copy, random=False, water=True)
            random_greedy.run()
        elif user.algorithm_p == 'greedy':
            random_greedy = RandomGreedy(amstelhaege_copy, random=False)
            random_greedy.run()
        elif user.algorithm_p == 'genetic':
            genetic = Genetic(amstelhaege_copy, user.neighbourhood, user.houses)
            amstelhaege_copy = genetic.run()

        # improve on the placement with the chosen algorithm        
        if user.algorithm_i == 'hillclimber random':
            hillclimber_random = HillclimberRandom(amstelhaege_copy)
            hillclimber_random.run()
        elif user.algorithm_i == 'simulated annealing':
            hillclimber_random = HillclimberRandom(amstelhaege_copy, True)
            hillclimber_random.run()       
        elif user.algorithm_i == 'hillclimber step':
            hillclimber_step = HillclimberStep(amstelhaege_copy)
            hillclimber_step.run()
        elif user.algorithm_i == 'hillclimber swap':
            hillclimber3 = HillclimberSwap(amstelhaege_copy)
            hillclimber_swap.run()

        new_score = amstelhaege_copy.price

        # check if the new price is higher and if so, save the map
        if new_score > highest_score:
            best_map = deepcopy(amstelhaege_copy)
            highest_score = new_score

        total_score += new_score

    return best_map, highest_score, total_score/user.iterations

