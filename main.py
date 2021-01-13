import sys
from code.classes.Amstelhaege import Amstelhaege
from code.classes.House import House
from visualise import visualise
from random import randrange
from output import output
from code.algorithms.random_placement import random_placement
from code.algorithms.random_greedy import random_greedy
from code.algorithms.hillclimber1 import Hillclimber_1
from code.helpers.repeat import repeat
from time import sleep



if __name__ == '__main__':
    
    # checks if correct amount of arguments are givem
    if len(sys.argv) != 4:
        print("Error: wrong input use: [neighbourhood map] [number of houses]")
        print("neigbourhood map: choose 0, 1 or 2")
        print("number of houses: choose 20, 40 or 60")    
    else:
        # 0 for wijk_1, 1 for wijk_2, 2 for wijk_3
        water_map = int(sys.argv[1])

        # maximum number of houses
        n_houses = int(sys.argv[2])

        # sets default maximum houses to 20
        if ((n_houses != 20) and (n_houses != 40) and (n_houses != 60)):
            n_houses = 20
        
        # number of iterations for the algorithm
        iterations = int(sys.argv[3])
    
    amstelhaege = Amstelhaege(water_map, n_houses)
 
    #_____________________ random algorithm _____________________
    # amstelhaege, price = repeat(amstelhaege, iterations, 'random')

    #_____________________ hillclimber 1 algorithm _____________________
    amstelhaege, price = repeat(amstelhaege, iterations, 'hillclimber')


    #voor random_greedy
    # amstelhaege, high_score = random_greedy(water_map,  n_houses, amstelhaege)

    #_____________________ result processing __________________________
    # visualising the results
    visualise(amstelhaege.waters, amstelhaege.houses, price)

    # formatting the final output file output.csv
    output(amstelhaege.houses, amstelhaege.waters, price)

    print("The results are.....")
    sleep(1)
    print(f"Your neighbourhood is worth {price} euro! Amazing!")