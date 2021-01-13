from random import randrange
from code.classes.Amstelhaege import Amstelhaege
from copy import deepcopy

def random_greedy(iterations, amstelhaege):
    """
    function that tries to place the house in random places and places it on the
    best position for the specific house
    """
    highest_score = 0

    for i in range(iterations):
        # x = randrange(amstelhaege.length)
        # y = randrange(amstelhaege.width)


        random_placement(amstelhaege)

        # checks if the move is valid
        amstelhaege.place_house(x,y)
        if amstelhaege.check_location(x, y, length, width, extra):
            score = amstelhaege.calculate_worth()

        # selects best place for the house
        if score > highest_score:
            highest_score = score
            best_x = x
            best_y = y
    
    # places house in best place
    amstelhaege.place_house(best_x, best_y)
    

# def place_house_greedy(neighbourhood):
#     """
#     creates house and runs greedy on it
#     """
#     if name =! water:
#         for house in neighbourhood.houses:
#             neighbourhood.append(house)
#             greedy_random(iterations, neighbourhood, house)



def greedy():
    """
    check 40 possible places for each next house
    """
    highest_score = 0
    #place water 


   
    # calculate number of houses for each house type
    numb_eengezinswoning = amstelhaege.fraction_house_1 * total
    numb_bungalow = amstelhaege.fraction_house_2 * total
    numb_maison = amstelhaege.fraction_house_3 * total

    # randomly places first house, which is maison
    x = randrange(amstelhaege.length)
    y = randrange(amstelhaege.width)
    amstelhaege.place_house(3, x, y)

    numb_maison = numb_maison + 1

    # consider 20 different places for house, select best one
    for number in range(house_number - 1):
        house_id = number + 2

        #check which house needs to be placed
        if numb_maison > 0:
            house_type = 3
            numb_maison = numb_maison - 1
        elif numb_bungalow > 0:
            house_type = 2
            numb_bungalow = numb_bungalow - 1
        elif numb_eengezinswoning > 0:
            house_type = 1
            numb_eengezinswoning = numb_eengezinswoning - 1


        tries = 0
        while tries < 40:
            placed = False

            # generate coordinates
            while placed == False:
                x = randrange(amstelhaege.length)
                y = randrange(amstelhaege.width)
                
                if amstelhaege.check_location(x, y, length, width, extra):
                    placed = True
                
            # calculate the worth
            score = amstelhaege.calculate_worth()
            if score > highest_score:
                highest_score = score
                best_x = x
                best_y = y
            
            tries += 1
