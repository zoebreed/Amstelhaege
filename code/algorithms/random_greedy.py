from code.classes.Amstelhaege import House
from random import randrange
from code.classes.Amstelhaege import Amstelhaege


def random_greedy(choice, n_houses, amstelhaege):
    """
    function that tries to place the house in random places and places it on the
    best position for the specific house
    """
    highest_score = 0
    total = n_houses

    #place water 
    amstelhaege = Amstelhaege(choice, n_houses)

    # calculate number of houses for each house type
    numb_eengezinswoning = amstelhaege.fraction_house_1 * total
    numb_bungalow = amstelhaege.fraction_house_2 * total
    numb_maison = amstelhaege.fraction_house_3 * total

    # randomly places first house, which is maison
    best_x = randrange(amstelhaege.length)
    best_y = randrange(amstelhaege.width)
    house_type = 3
    new_house = House(best_x, best_y, house_type)
    new_house.total_freearea = 20
    # amstelhaege.get_free_space()
    # new_house.length= 12
    # new_house.width = 10
    # new_house.increase_value = 0.06
    # new_house.value = 610000
    # new_house.free_area = 6


    amstelhaege.houses.append(new_house)
    amstelhaege.neighbourhood.append(new_house)
  
    amstelhaege.calculate_worth()
    score = amstelhaege.price


    print(amstelhaege.houses)
    print(score)

    numb_maison = numb_maison + 1

    # consider 40 different places for house, select best one
    for number in range(total - 1):
        #check which house needs to be placed
        if numb_maison > 0:
            house_type = 3
            length, width, extra = 12, 10, 6
            numb_maison -=  1
        elif numb_bungalow > 0:
            house_type = 2
            length, width, extra = 11, 7, 3
            numb_bungalow -= 1
        elif numb_eengezinswoning > 0:
            house_type = 1
            length, width, extra = 8, 8, 2
            numb_eengezinswoning -= 1
        

        amstelhaege.place_house(house_type, best_x, best_y)
        amstelhaege.get_free_space()
        
        #TODO: wil je deze tries zelf kunnen bepalen?
        tries = 0
        while tries < 5:
            placed = False

            # generate coordinates
            while placed == False:
                x = randrange(amstelhaege.length)
                y = randrange(amstelhaege.width)
                
                if amstelhaege.check_location(x, y, length, width, extra):
                    placed = True
                
            # selects best place for the house
            amstelhaege.calculate_worth()
            score = amstelhaege.price
            # print(highest_score)
            if score > highest_score:
                highest_score = score
                best_x = x
                best_y = y
            
            tries += 1

    return amstelhaege, highest_score


#    highest_score = 0

#     for i in range(iterations):
#         # x = randrange(amstelhaege.length)
#         # y = randrange(amstelhaege.width)
#         random_placement(amstelhaege)

#         # checks if the move is valid
#         amstelhaege.place_house(x,y)
#         if amstelhaege.check_location(x, y, length, width, extra):
#             score = amstelhaege.calculate_worth()

#         # selects best place for the house
#         if score > highest_score:
#             highest_score = score
#             best_x = x
#             best_y = y
    
#     # places house in best place
#     amstelhaege.place_house(best_x, best_y)
    