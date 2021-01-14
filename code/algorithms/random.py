from random import randrange
from code.classes.Amstelhaege import Amstelhaege
from copy import deepcopy
    
def random(amstelhaege):
    """
    algorithm which places the houses in a random location
    """
    total = amstelhaege.total

    for i in range(int(amstelhaege.fraction_house_1*total)):
        check = True
        width, length, extra = 8, 8, 2

        while check:
            
            # generate random coordinates
            x = randrange(amstelhaege.width)
            y = randrange(amstelhaege.length)

            # check if the coordinates are valid
            if amstelhaege.check_location(x, y, length, width, extra):
                amstelhaege.place_house(1, x, y)
                check = False

        check = True

    for i in range(int(amstelhaege.fraction_house_2*total)):
        check = True
        width, length, extra = 11, 7, 3

        while check:
            x = randrange(amstelhaege.width)
            y = randrange(amstelhaege.length)
            if amstelhaege.check_location(x, y, length, width, extra):
                amstelhaege.place_house(2, x, y)
                check = False
        
        check = True

    for i in range(int(amstelhaege.fraction_house_3*total)):
        check = True
        width, length, extra = 12, 10, 6

        while check:
            x = randrange(amstelhaege.width)
            y = randrange(amstelhaege.length)

            if amstelhaege.check_location(x, y, width, length, extra):
                amstelhaege.place_house(3, x, y)
                check = False
        check = True
    
    amstelhaege.get_free_space()
    amstelhaege.calculate_worth()
    
    return amstelhaege