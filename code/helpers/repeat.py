from code.algorithms.randomize import Random
from code.algorithms.hillclimber1 import Hillclimber_1
from code.algorithms.hillclimber2 import Hillclimber_2
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

        elif user.algorithm_p == 'random_greedy':
            random_greedy = Random_greedy(amstelhaege_copy, sim_ann=True)
            random_greedy.run(400)

        # then improve on the placement with the chosen algorithm        
        if user.algorithm_i == 'hillclimber':
            hillclimber1 = Hillclimber_1(amstelhaege_copy)
            hillclimber1.run()

        elif user.algorithm_i == 'simulated annealing':
            hillclimber1 = Hillclimber_1(amstelhaege_copy, True)
            hillclimber1.run()       
        
        elif user.algorithm_i == 'hillclimber2':
            hillclimber2 = Hillclimber_2(amstelhaege_copy)
            hillclimber2.run(1)

        new_score = amstelhaege_copy.price

        # check if the new price is higher and if so, save the map
        if new_score > highest_score:
            best_map = deepcopy(amstelhaege_copy)
            highest_score = new_score

        total_score += new_score

        print(new_score)
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

