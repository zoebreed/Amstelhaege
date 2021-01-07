from code.classes.Amstelhaege import Amstelhaege
from code.classes.House import House
from code.classes.Water import Water
from visualise import visualise
import matplotlib
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
from random import randrange

if __name__ == '__main__':
    houses = []
    for x in range(10):
        x1 = randrange(150)
        y1 = randrange(150)
        house = House(x1, y1, x1+5, y1+5, 1, 1)
        houses.append(house)
    
    neighbourhood = Amstelhaege.load_water
    visualise(neighbourhood, houses)
