import matplotlib
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
# # from /code/classes/House.py import House
# # from code.classes.House import House
# # from .house import House
from random import randrange

def visualise(neighbourhood, houses):
    """
    Function which visualises the map
    """

    fig, ax = plt.subplots()

    #TODO geef free area een lichtere kleur met alpha = ...

    # for water in neighbourhood:
    #     # get the coordinates and specifications of the water
    #     x, y = water.x_bottom_left, water.y_bottom_left
    #     ax.add_patch(Rectangle((x, y), height, width, edgecolor = 'blue', facecolor = color, fill=True))

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
    # plt.figure(figsize=(160,180))
    plt.plot(x,y)
    # plt.xlim(180)
    # plt.ylim(160)
    # plt.legend()
    plt.title("Amstelhaege")
    plt.savefig("test.png")
    # plt.show()





