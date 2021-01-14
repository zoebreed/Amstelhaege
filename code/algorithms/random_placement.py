from random import randrange
from code.classes.Amstelhaege import Amstelhaege
from copy import deepcopy

# def random_algorithm(iterations, amstelhaege, choice, n_houses):
#     """
#     repeats the random_placement algorithm with a choosen number of iterations
#     """
#     highest_score, scores = 0, []

#     for i in range(iterations):
       
#         # amstelhaege.load_water(choice)
#         # new_map = random_placement(amstelhaege)
        
#         amstelhaege = Amstelhaege(choice, n_houses)
#         random_placement(amstelhaege)
#         new_score = amstelhaege.price
   
#         if new_score > highest_score:
#             best_map = deepcopy(amstelhaege)
#             highest_score = new_score

#         scores.append([i, new_score])
    
#     return best_map, highest_score
    
def random_placement(amstelhaege):
    """
    algorithm which places the houses in a random location
    """
    total = amstelhaege.total

    for i in range(int(amstelhaege.fraction_house_1*total)):
        check = True
        length, width, extra = 8, 8, 2

        while check:
            
            # generate random coordinates
            x = randrange(amstelhaege.length)
            y = randrange(amstelhaege.width)

            # check if the coordinates are valid
            if amstelhaege.check_location(x, y, length, width, extra):
                amstelhaege.place_house(1, x, y)
                check = False

        check = True

    for i in range(int(amstelhaege.fraction_house_2*total)):
        check = True
        length, width, extra = 11, 7, 3

        while check:
            x = randrange(amstelhaege.length)
            y = randrange(amstelhaege.width)
            if amstelhaege.check_location(x, y, length, width, extra):
                amstelhaege.place_house(2, x, y)
                check = False
        
        check = True

    for i in range(int(amstelhaege.fraction_house_3*total)):
        check = True
        length, width, extra = 12, 10, 6

        while check:
            x = randrange(amstelhaege.length)
            y = randrange(amstelhaege.width)

            if amstelhaege.check_location(x, y, length, width, extra):
                amstelhaege.place_house(3, x, y)
                check = False
        check = True
    
    amstelhaege.get_free_space()
    amstelhaege.calculate_worth()
    
    return amstelhaege