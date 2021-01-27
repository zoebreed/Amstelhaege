from code.algorithms.water_greedy import WaterGreedy
from code.parameters import iters
from random import randrange

class RandomGreedy():
    """
    Function that tries to place the house in random locations and places it on the
    best position for the specific house

    :param amstelhaege: The object amstelhaege
    :param random: Whether to place the houses randomly, default is True
    :param water: Whether to place the house greedy, default is False
    """

    def __init__(self, amstelhaege, random=True, water=False):
        self.amstelhaege = amstelhaege
        self.random = random
        self.highest_score = None
        self.score = None   

        if self.random:
            self.amount1 = 1
            self.amount2 = iters.randomGreedy
        elif not random:
            self.amount1 = self.amstelhaege.width
            self.amount2 = self.amstelhaege.length

        self.water = water
        if self.water:
            self.waters = WaterGreedy()

    def run(self):
        """
        Runs the algorithm with the chosen settings
        :return: The amstelhaege object with the houses and water placed
        """
            
        # consider different places for the house, select best one
        for j in [3, 2, 1]:
            house_info = self.amstelhaege.house[j]
            for i in range(int(house_info.percentage * self.amstelhaege.total)):
                self.highest_score = 0

                # creates house object at an arbitrary location outside the map
                house = self.amstelhaege.place_house(house_info.type, -100, -100)
                
                for x in range(self.amount1):
                    for y in range(self.amount2):
                        placed, placed2 = False, False

                        # generate random coordinates
                        while placed == False:
                            if self.random:
                                x = randrange(self.amstelhaege.width)
                                y = randrange(self.amstelhaege.length)
                            else:
                                placed = True
                            
                            # check if the coordinates are available
                            if self.amstelhaege.check_location(x, y, house):
                                if self.water:
                                    check, temp = self.waters.check_water(x, y, house.width, house.length)
                                    if check:
                                        waters = temp
                                        house.move(x, y)
                                        placed, placed2 = True, True
                                else:
                                    house.move(x,y)
                                    placed, placed2 = True, True

                        if self.random == True or placed2 == True:
                            # calculates worth of the map      
                            self.amstelhaege.calculate_price()
                            self.score = self.amstelhaege.price
                       
                            # if score is higher than the currrent, save the position
                            if self.score > self.highest_score:
                                x_max = house.x_left
                                y_max = house.y_bottom
                                self.highest_score = self.score

                                if self.water:
                                    waters_max = waters

                if self.water:    
                    self.waters.waters = waters_max

                # places the hous in the best position and updates the score
                house.move(x_max, y_max)
                self.amstelhaege.calculate_price()
        
        if self.water:    
            self.waters.minimize()
            self.amstelhaege.load_water2(self.waters.waters)

        return self.amstelhaege