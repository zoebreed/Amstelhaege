import sys
from user_input import User
from code.classes.Amstelhaege import Amstelhaege
from code.classes.House import House
from visualise import visualise
from random import randrange
from output import output
from code.algorithms.random import random
from code.algorithms.random_greedy import Random_greedy
from code.algorithms.hillclimber1 import Hillclimber_1
from code.algorithms.hillclimber2 import Hillclimber_2
from code.helpers.repeat import repeat
from time import sleep

    
if __name__ == '__main__':    
    
    user = User()

    amstelhaege = Amstelhaege(user.neighbourhood, user.houses)
    amstelhaege, best_price, avg_price = repeat(amstelhaege, user.iterations, user.algorithm)
    
    #_____________________ result processing __________________________

    # visualising the results
    visualise(amstelhaege.waters, amstelhaege.houses, price)

    # formatting the final output file output.csv
    output(amstelhaege.houses, amstelhaege.waters, price)

    print("_____________________________")
    print("The results are.....")
    sleep(1)
    print(f"The best neighbourhood you found is {best_price} euro! Amazing!")
    print(f"The average price of the neighbourhoods you found is  {best_price} euro!")
