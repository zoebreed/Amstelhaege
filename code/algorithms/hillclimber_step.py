from code.algorithms.hillclimber import Hillclimber
from random import choice

class HillclimberStep(Hillclimber):
    """
    Executes the step version of the hillclimber algorithm. As input
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

        # save the original coordinates for later
        x, y = house.x_left, house.y_bottom

        for direction in self.directions:
            new_coordinates = self.hillclimber_step_move(house, direction)

            # move the house temporarily outside of the map to prevent overlap on itself
            house.move()
            
            if self.amstelhaege.check_location(new_coordinates[0], new_coordinates[1], house):
                house.move(new_coordinates[0], new_coordinates[1])
            else: 
                house.move(x, y)

            # get the difference between the old and new price
            price_diff = self.price_diff(old_price)

            # if the move in a direction yields a higher price, save the direction and update the old price
            if not self.price_check(price_diff):
                best_direction = direction
                old_price = self.amstelhaege.price
            
            # move house back to original position, to compare the directions with this position
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
                x, y = house.x_left, house.y_bottom

                # get the initial price
                old_price = self.amstelhaege.calculate_price()

                new_coordinates = self.hillclimber_step_move(house, direction)
                
                if direction is not None: 
                    # move the house temporarily outside of the map to prevent overlap on itself
                    house.move()
                    # make the move, if the move is possible. Ohterwise keep the initial place
                    if self.amstelhaege.check_location(new_coordinates[0], new_coordinates[1], house):
                        house.move(new_coordinates[0], new_coordinates[1])
                    else: 
                        house.move(x, y)

                new_price = self.amstelhaege.calculate_price()

                # move decreases the worth
                if new_price < old_price:
                    house.move(x, y)
                
                self.amstelhaege.calculate_price()

        return self.amstelhaege