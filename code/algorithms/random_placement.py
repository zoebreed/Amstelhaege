from random import randrange

def random_placement(amstelhaege):
    """
    algorithm which places the houses in a random location
    """
    total = amstelhaege.total

    for i in range(int(amstelhaege.fraction_house_1*total)):
        check = True
        width = 8
        length = 8
        extra = 2

        while check:
            x = randrange(amstelhaege.length)
            y = randrange(amstelhaege.width)

            if amstelhaege.check_location(x, y, length, width, extra):
                amstelhaege.place_house(1, x, y)
                check = False

        check = True

    for i in range(int(amstelhaege.fraction_house_2*total)):
        check = True
        width = 11
        length = 7
        extra = 3

        while check:
            x = randrange(amstelhaege.length)
            y = randrange(amstelhaege.width)
            if amstelhaege.check_location(x, y, length, width, extra):
                amstelhaege.place_house(2, x, y)
                check = False
        
        check = True

    for i in range(int(amstelhaege.fraction_house_3*total)):

        check = True
        width = 12
        length = 10
        extra = 6

        while check:
            x = randrange(amstelhaege.length)
            y = randrange(amstelhaege.width)

            if amstelhaege.check_location(x, y, length, width, extra):
                amstelhaege.place_house(3, x, y)
                check = False
        check = True


