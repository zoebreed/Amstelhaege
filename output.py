import csv
from code.classes.House import House
from code.classes.Water import Water

def output(neighbourhood):
    with open('output.csv', 'w', newline='') as csvfile:
        wr = csv.writer(csvfile)
        wr.writerow(['structure', 'corner_1', 'corner_2', 'corner_3', 'corner_4', 'type'])
        
        #TODO: structure en type nog aanpassen in het model
        for item in neighbourhood:
            if isinstance(item, House):
                corn1 = f"{item.x_bottom_left}, {item.y_top_right}"
                corn2 = f"{item.x_bottom_left}, {item.y_bottom_left}"
                corn3 = f"{item.x_top_right}, {y_bottom_left}"
                corn4 = f"{item.x_top_right}, {y_top_right}"
                wr.writerow(['struc', corn1, corn2, corn3, corn4, item.house_type])
            # elif isinstance(item, Water):

        #TODO: networth
        networth = 0
        wr.writerow(['networth', networth])