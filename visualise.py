import matplotlib
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
# # from /code/classes/House.py import House
# # from code.classes.House import House
# # from .house import House
from random import randrange

def visualise(waters, houses):
    """
    Function which visualises the map
    """
    #TODO geef free area een lichtere kleur met alpha = ...

    fig, ax = plt.subplots()

    for water in waters:
        if water.name == "Water":
            # get the coordinates and specifications of the water
            x, y = water.x_bottom_left, water.y_bottom_left
            ax.add_patch(Rectangle((x, y), water.height, water.width, facecolor = 'lightblue', fill=True))

    for house in houses:
        # get the coordinates and specifications of the house
        x, y = house.x_bottom_left, house.y_bottom_left
        height, width = house.length, house.width

        if house.house_type == 1:
            color = 'red'
        elif house.house_type == 2:
            color = 'green'
        else:
            color = 'yellow'

        ax.add_patch(Rectangle((x, y), height, width, edgecolor = 'black', facecolor = color, fill=True))
    
    plt.plot(x,y)
    plt.xlim(left = 0, right=160)
    plt.ylim(bottom= 0, top=180)
    plt.title("Amstelhaege")
    plt.savefig("test.jpeg")





