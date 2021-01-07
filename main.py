import sys
from code.classes.Amstelhaege import Amstelhaege
from code.classes.House import House
from visualise import visualise
from random import randrange
from output import output
from code.algorithms.random_placement import random_placement

if __name__ == '__main__':

    
    # 0 for wijk_1, 1 for wijk_2, 2 for wijk_3
    water_map = int(sys.argv[1])
        
    amstelhaege = Amstelhaege(water_map)
    random_placement(amstelhaege)

    waters = amstelhaege.waters
    visualise(waters, amstelhaege.houses)

    visualise(waters, amstelhaege.houses)
    # voor nu geef ik waters als parameter omdat de neighbourhoods returnt
    output(waters)