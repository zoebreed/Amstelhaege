import sys
from code.classes.Amstelhaege import Amstelhaege
from code.classes.House import House
from visualise import visualise
from random import randrange
from output import output

if __name__ == '__main__':
    
     # 0 for wijk_1, 1 for wijk_2, 2 for wijk_3
    water_map = int(sys.argv[1])
    
    houses = []
    for x in range(10):
        x1 = randrange(150)
        y1 = randrange(150)
        house = House(x1, y1, x1+5, y1+5, 1, 1)
        houses.append(house)
    
    waters = Amstelhaege.load_water(water_map)
    visualise(waters, houses)
    # voor nu geef ik waters als parameter omdat de neighbourhoods returnt
    output(waters)