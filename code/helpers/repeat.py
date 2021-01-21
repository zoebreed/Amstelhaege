from code.algorithms.random import Random
from code.algorithms.hillclimber1 import Hillclimber1
from code.algorithms.hillclimber2 import Hillclimber2
from code.algorithms.hillclimber3 import Hillclimber3
from code.algorithms.random_greedy import Random_greedy
from copy import deepcopy
import csv

def repeat(amstelhaege, user):
    """
    repeats the given algorithm n times and gets the best result
    """
    highest_score, total_score = 0, 0

    for i in range(user.iterations):

        amstelhaege_copy = deepcopy(amstelhaege)

        # first place the houses using the chosen algorithm
        if user.algorithm_p == 'random':
            random = Random(amstelhaege_copy)
            random.run()
        elif user.algorithm_p == 'random_greedy' and user.neighbourhood == 'greedy_water':
            random_greedy = Random_greedy(amstelhaege_copy, water=True)
            random_greedy.run()
        elif user.algorithm_p == 'random_greedy':
            random_greedy = Random_greedy(amstelhaege_copy)
            random_greedy.run()
        elif user.algorithm_p == 'greedy' and user.neighbourhood == 'greedy_water':
            random_greedy = Random_greedy(amstelhaege_copy, random=False, water=True)
            random_greedy.run()
        elif user.algorithm_p == 'greedy':
            random_greedy = Random_greedy(amstelhaege_copy, random=False)
            random_greedy.run()
        elif user.algorithm_p == 'genetic':
            genetic = Genetic(amstelhaege_copy)
            amstelhaege_copy = genetic.run()

        # then improve on the placement with the chosen algorithm        
        if user.algorithm_i == 'hillclimber':
            hillclimber1 = Hillclimber1(amstelhaege_copy)
            hillclimber1.run()
        elif user.algorithm_i == 'simulated annealing':
            hillclimber1 = Hillclimber1(amstelhaege_copy, True)
            hillclimber1.run()       
        elif user.algorithm_i == 'hillclimber2':
            hillclimber2 = Hillclimber2(amstelhaege_copy)
            hillclimber2.run()
        elif user.algorithm_i == 'hillclimber3':
            hillclimber3 = Hillclimber2(amstelhaege_copy)
            hillclimber3.run()

        new_score = amstelhaege_copy.price

        # check if the new price is higher and if so, save the map
        if new_score > highest_score:
            best_map = deepcopy(amstelhaege_copy)
            highest_score = new_score

        total_score += new_score

        #iteratie,wijk,huizenvariant,prijs
        if user.algorithm_p == 'random' and user.algorithm_i == 'hillclimber':
            with open('results/hillclimber1_r.csv', 'a', newline='') as csvfile:
                wr = csv.writer(csvfile)
                wr.writerow([i, user.neighbourhood, user.houses, new_score])
        elif user.algorithm_p == 'random' and user.algorithm_i == 'hillclimber2':
            with open('results/hillclimber2_r.csv', 'a', newline='') as csvfile:
                wr = csv.writer(csvfile)
                wr.writerow([i, user.neighbourhood, user.houses, new_score])
        elif user.algorithm_p == 'random_greedy' and user.algorithm_i == 'hillclimber':
            with open('results/hillclimber1_rg.csv', 'a', newline='') as csvfile:
                wr = csv.writer(csvfile)
                wr.writerow([i, user.neighbourhood, user.houses, new_score])
        elif user.algorithm_p == 'random_greedy' and user.algorithm_i == 'hillclimber2':
            with open('results/hillclimber2_rg.csv', 'a', newline='') as csvfile:
                wr = csv.writer(csvfile)
                wr.writerow([i, user.neighbourhood, user.houses, new_score])
        elif user.algorithm_p == 'random' and user.algorithm_i == 'None':
            with open('results/random.csv', 'a', newline='') as csvfile:
                wr = csv.writer(csvfile)
                wr.writerow([i, user.neighbourhood, user.houses, new_score])
        elif user.algorithm_p == 'random_greedy' and user.algorithm_i == 'None':
            with open('results/random_greedy.csv', 'a', newline='') as csvfile:
                wr = csv.writer(csvfile)
                wr.writerow([i, user.neighbourhood, user.houses, new_score])


    return best_map, highest_score, total_score/user.iterations

