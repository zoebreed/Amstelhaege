import matplotlib
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
from random import randrange

def visualise(waters, houses, price):
    """
    Function which visualises the map
    """

    fig, ax = plt.subplots()

    for water in waters:
        if water.name == "water":
            # get the coordinates and specifications of the water
            x, y = water.x_left, water.y_bottom
            ax.add_patch(Rectangle((x, y), water.height, water.width, edgecolor = 'lightskyblue', facecolor = 'lightskyblue', fill=True))

    for house in houses:
        # get the coordinates and specifications of the house
        x, y = house.x_left, house.y_bottom
        plt.text(x, y,house.total_freearea)
        height, width = house.length, house.width

        # get the coordinates and specifications of the free space
        x2, y2 = x - house.total_freearea, y - house.total_freearea
        height2, width2 = house.length + 2*house.total_freearea, house.width + 2*house.total_freearea

        if house.house_type == 1:
            color = 'firebrick'
        elif house.house_type == 2:
            color = 'darkorange'
        else:
            color = 'salmon'
        
        ax.add_patch(Rectangle((x2, y2), height2, width2, facecolor = 'gray', fill=True, edgecolor=None, alpha=0.5))
        ax.add_patch(Rectangle((x, y), height, width, facecolor = color, fill=True))

    
    plt.plot(x,y)
    plt.xlim(left = 0, right=160)
    plt.ylim(bottom= 0, top=180)
    ax.set_facecolor("palegreen")
    plt.title(f"€{price}")
    plt.savefig("results/test.png")