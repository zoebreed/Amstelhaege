import csv
from code.classes.House import House
from code.classes.Water import Water

def output(neighbourhood):
    with open('results/output.csv', 'w', newline='') as csvfile:
        wr = csv.writer(csvfile)
        wr.writerow(['structure', 'corner_1', 'corner_2', 'corner_3', 'corner_4', 'type'])
        
        counter = 1
        structures = []

        for item in neighbourhood:
            if item.name not in structures:
                counter = 1

            corn1 = f"{item.x_bottom_left},{item.y_top_right}"
            corn2 = f"{item.x_bottom_left},{item.y_bottom_left}"
            corn3 = f"{item.x_top_right},{item.y_bottom_left}"
            corn4 = f"{item.x_top_right},{item.y_top_right}"
            struc = f"{item.name}_{counter}"
            wr.writerow([struc, corn1, corn2, corn3, corn4, item.name.upper()])

            structures.append(item.name)
            counter += 1

        #TODO: networth
        networth = 0
        wr.writerow(['networth', networth])