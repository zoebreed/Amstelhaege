import sys
from code.classes.Amstelhaege import Amstelhaege
from code.classes.House import House
from visualise import visualise
from random import randrange
from output import output
from code.algorithms.random_placement import random_placement

if __name__ == '__main__':
    
    # checks if correct amount of arguments are givem
    if len(sys.argv) != 3:
        print("Error: wrong input use: [neighbourhood map] [number of houses]")
        print("neigbourhood map: choose 0, 1 or 2")
        print("number of houses: choose 20, 40 or 60")    
    else:
        # 0 for wijk_1, 1 for wijk_2, 2 for wijk_3
        water_map = int(sys.argv[1])

        # maximum number of houses
        n_houses = int(sys.argv[2])

        #TODO volgens mij kan deze korter
        # sets default maximum houses to 20
        if ((n_houses != 20) and (n_houses != 40) and (n_houses != 60)):
            n_houses = 20
        
    amstelhaege = Amstelhaege(water_map, n_houses)
    random_placement(amstelhaege)
    amstelhaege.random_free_space()

    waters = amstelhaege.waters
    visualise(waters, amstelhaege.houses, amstelhaege.price)

    output(amstelhaege.neighbourhood, amstelhaege.price)