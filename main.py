from code.helpers.output import output
from code.helpers.user_input import User
from code.helpers.visualise import visualise
from code.classes.Amstelhaege import Amstelhaege
from code.helpers.repeat import repeat
from time import sleep
    
if __name__ == '__main__':    
    
    user = User()

    amstelhaege = Amstelhaege(user.neighbourhood, user.houses)
    amstelhaege, best_price, avg_price = repeat(amstelhaege, user)
    
    #_____________________ result processing __________________________

    # visualising the results
    visualise(amstelhaege.waters, amstelhaege.houses, best_price)

    # formatting the final output file output.csv
    output(amstelhaege.houses, amstelhaege.waters, best_price)

    print("_____________________________")
    print("The results are.....")
    sleep(1)
    print(f"The best neighbourhood you found is {best_price} euro! Amazing!")
    print(f"The average price of the neighbourhoods you found is  {avg_price} euro!")