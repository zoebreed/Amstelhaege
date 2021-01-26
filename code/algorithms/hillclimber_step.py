from random import choice
from code.algorithms.hillclimber import Hillclimber

class HillclimberStep(Hillclimber):
    """
    Executes the second version of the hillclimber algorithm. As input
    it takes amstelhaege with the houses already placed. Then a random 
    is moved in the direct with the biggest price gain.
    """
    def __init__(self, amstelhaege, sim_ann=False):

        Hillclimber.__init__(self, amstelhaege, sim_ann)
        self.directions = ["up", "down", "right", "left"]

    def hillclimber_step_move(self, house, direction):
        """
        :param direction: string of the direction
        :param house: house object
        :return: The x_left and y_bottom coordinates according to the direction
        """
        # coordinates in new coordinates: [x_left, y_bottom]
        if direction == "up":
            self.new_coordinates = [house.x_left, house.y_bottom + 1]
        elif direction == "down":
            self.new_coordinates = [house.x_left, house.y_bottom - 1]
        elif direction == "right":
            self.new_coordinates = [house.x_left + 1, house.y_bottom]
        elif direction == "left": 
            self.new_coordinates = [house.x_left - 1, house.y_bottom]

        return self.new_coordinates

    def find_best_direction(self, house):
        """
        :param house: house_object
        :return: the direction which will yield the biggest price gain (string)
        """
        best_direction = None
        old_price = self.amstelhaege.price
        for direction in self.directions:
            x = house.x_left
            y = house.y_bottom

            new_coordinates = self.hillclimber_step_move(house, direction)

            house.move(-100, -100)
            
            if self.amstelhaege.check_location(new_coordinates[0], new_coordinates[1], house.width, house.length, house.free_area):
                house.move(new_coordinates[0], new_coordinates[1])
            else: 
                house.move(x, y)

            price_diff = self.price_diff(old_price)
        
            if not self.price_check(price_diff):
                best_direction = direction
            else:
                house.move(x, y)

        return best_direction
  
    def run(self):
        """
        Runs the hillclimber algorith with the user chosen settings
        :return: The amstelhaege object with the improved house placement
        """

        old_price = self.amstelhaege.price

        # stop if the given time has passed
        while self.condition():

            house = choice(self.amstelhaege.houses)
            direction = self.find_best_direction(house)

            # make sure that at the start of each house and each direction you get in the while loop 
            new_price = self.amstelhaege.price + 1

            # keep stepping into the same direction if the move increases the worth
            while new_price > old_price:
                # save the initial coordinates
                x = house.x_left
                y = house.y_bottom

                # get the initial price
                old_price = self.get_price()

                new_coordinates = self.hillclimber_step_move(house, direction)
                
                if direction is not None: 
                    # move the house temporarily outside of the map to prevent overlap on itself
                    house.move(-100, -100)
                    # make the move, if the move is possible. Ohterwise keep the initial place
                    if self.amstelhaege.check_location(new_coordinates[0], new_coordinates[1], house.width, house.length, house.free_area):
                        house.move(new_coordinates[0], new_coordinates[1])
                    else: 
                        house.move(x, y)

                new_price = self.get_price()

                # move decreases the worth
                if new_price < old_price:
                    house.move(x, y)
                
                self.amstelhaege.get_free_space()
                self.amstelhaege.calculate_price()

                #print(f"house.id {house.id} highest score{new_price} current score {self.get_price()}")

        return self.amstelhaege

# __________________________old version ___________________________
    # def run(self, timeout):

    #     # # uses random algorithm to generate the first state
    #     # random(self.amstelhaege)
    #     old_price = self.amstelhaege.price

    #     timeout_start = time.time()

    #     # stop if the given time has passed
    #     while time.time() < timeout_start + timeout:
    #         # for house in self.amstelhaege.houses:
    #         house = choice(self.amstelhaege.houses)

    #         # shuffle the direction list to avoid a bias
    #         shuffle(self.directions)

    #         # go through every direction in the list
    #         for direction in self.directions:

    #             # make sure that at the start of each house and each direction you get in the while loop 
    #             new_price = self.amstelhaege.price + 1

    #             # keep stepping into the same direction if the move increases the worth
    #             while new_price > old_price:
    #                 # save the initial coordinates
    #                 x = house.x_left
    #                 y = house.y_bottom

    #                 # get the initial price
    #                 old_price = self.get_price()

    #                 new_coordinates = self.hillclimber2_move(house, direction)

    #                 # move the house temporarily outside of the map to prevent overlap on itself
    #                 house.move(-100, -100)
                    
    #                 # make the move, if the move is possible. Ohterwise keep the initial place
    #                 if self.amstelhaege.check_location(new_coordinates[0], new_coordinates[1], house.width, house.length, house.free_area):
    #                     house.move(new_coordinates[0], new_coordinates[1])
    #                 else: 
    #                     house.move(x, y)

    #                 new_price = self.get_price()

    #                 # move decreases the worth
    #                 if new_price < old_price:
    #                     house.move(x, y)
                    
    #                 self.amstelhaege.get_free_space()
    #                 self.amstelhaege.calculate_worth()

    #                 #print(f"house.id {house.id} highest score{new_price} current score {self.get_price()}")

    #     return self.amstelhaege

