class User:
    """
    class representing the user and their choices
    """
    
    def __init__(self):
        print("")
        print("Welcome to Amstelhaege!")
        print("")

        print("Which neighbourhood wood you like?")
        self.neighbourhood = self.get_neighbourhood()
        print('\n')
        
        print("And how many houses would you like to place?")
        self.houses = self.get_houses()
        print('\n')

        print("And which algorithm would you like to use to place the houses?")
        self.algorithm_p = self.get_p_algorithm(self.neighbourhood)
        print('\n')

        print("And which algorithm would you like to use?")
        self.algorithm_i = self.get_i_algorithm()
        print('\n')

        print("And for how many iterations would you like to run your code?")
        self.iterations = self.get_iterations()
        print('\n')


    def get_neighbourhood(self):
        """
        :return: the neighbourhood
        """
        neighbourhood_list = ["wijk1", "wijk2", "wijk3", "random water", "greedy water"]
        neighbourhood = input(f"Choose from: {', '.join(neighbourhood_list)}\n")

        if neighbourhood not in neighbourhood_list:
            print("You chose an invalid neighbourhood")
            neighbourhood = self.get_neighbourhood()

        if neighbourhood == "wijk1":
            return 0
        elif neighbourhood == "wijk2":
            return 1
        elif neighbourhood == "wijk3":
            return 2
        else:
            return(neighbourhood)
        
    def get_houses(self):
        """
        :return: the amount of houses
        """
        houses_list = ["20", "40", "60"]
        houses = input(f"Choose from: {', '.join(houses_list)}\n")

        if houses not in houses_list:
            print("You chose an invalid neighbourhood")
            houses = self.get_houses()
    
        return int(houses)

    def get_p_algorithm(self, neighbourhood):
        """
        :return: the algorithm which is used to place the houses
        """
        if neighbourhood == "greedy water":
            algorithm_list = ["greedy", "random greedy"]
        else:
            algorithm_list = ["random", "greedy", "random greedy", "genetic"]
        algorithm = input(f"Choose from: {', '.join(algorithm_list)}\n")

        if algorithm not in algorithm_list:
            print("You chose an invalid algorithm")
            algorithm = self.get_p_algorithm(neighbourhood)
    
        return algorithm

    
    def get_i_algorithm(self):
        """
        :return: the algorithm which is used to improve the placement
        """
        algorithm_list = ["None", "hillclimber random", "hillclimber step", "hillclimber swap", "simulated annealing"]
        algorithm = input(f"Choose from: {', '.join(algorithm_list)}\n")

        if algorithm not in algorithm_list:
            print("You chose an invalid algorithm")
            algorithm = self.get_i_algorithm()
    
        return algorithm
        
    def get_iterations(self):
        """
        :return: the amount of iterations
        """
        iterations = input("Please choose any natural number: ")

        if not iterations.isdigit():
            print("You didn't choose an integer")
            iterations = self.get_iterations()
   
        iterations = int(iterations)

        if iterations < 0:
            print("You must choose a positive integer!")
            iterations = self.get_iterations()
        
        return int(iterations)