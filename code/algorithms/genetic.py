"""
This genetic algorithm uses the phrases used in the explanation of the genetic algorithm on 
https://www.tutorialspoint.com/genetic_algorithms/index.htm
"""
from code.algorithms.random import Random
from code.algorithms.random_greedy import RandomGreedy
from code.classes.Amstelhaege import Amstelhaege
from code.algorithms.hillclimber_random import HillclimberRandom
from code.algorithms.hillclimber_swap import HillclimberSwap
from code.parameters import probs, gen
from copy import deepcopy
from random import random, choice, uniform

class Chromosome():
    """
    An object of this class is an individual from the population. It takes an area with the houses
    already placed. And it stores the area and the worth of an area as its fitness value. 
    """

    def __init__(self, amstelhaege):
        self.amstelhaege = amstelhaege
        self.cum_fitness = None
        self.fitness = self.amstelhaege.calculate_price()

    def mutate(self):
        """
        Mutates an individual from the population by swapping houses and/or moving houses to
        random coordinates.
        """
        self.swap_houses()
        self.move_houses()

    def swap_houses(self):
        """
        Swaps the position of two houses with a mutationprobability.
        """
        for house in self.amstelhaege.houses:
            r = random()
            if r < probs.mutation:
                
                # choose a random house to swap with
                house2 = choice(self.amstelhaege.houses)
                if house == house2:
                    continue
                
                # use the swap function in the hillclimber_swap algorithm to swap the houses
                hillclimber_swap = HillclimberSwap(self.amstelhaege)
                if hillclimber_swap.swap(house, house2):
                    self.amstelhaege.get_free_space()
                    self.fitness = self.amstelhaege.calculate_price()

    def move_houses(self):
        """
        Moves a house to a random position with a mutation probability.
        """
        for house in self.amstelhaege.houses:
            r = random()
            if r < probs.mutation:
                # use the move house random function in the hillclimber_random algorithm to move the house
                hillclimber_random = HillclimberRandom(self.amstelhaege)
                hillclimber_random.move_house_random(house)
        
                self.amstelhaege.get_free_space()
                self.fitness = self.amstelhaege.calculate_price()

class Genetic():
    """
    Executes the genetic algorithm. As input it takes an empty amstelhaege area with the inputted 
    choice for the neighbourhood and number of houses. It initializes a population of individual 
    'chromosomes' with the random_greedy or greedy algorithm. Using their fitness values, random 
    parents are selected for reproduction. 

    Then repeatedly: 
    1. Parents are used to reproduce, to make new solutions (children)
    2. These children are mutated to prevent the new generation to be homogenous
    3. A new generation is created with the best individuals out of the group of parents and children
    4. The new generation become the new parents

    This is done until the average of generation converges and does not increase anymore. 

    :param amstelhaege: The object amstelhaege
    :param neighbourhood: The neighbourhoodchoice
    :param houses: The number of houses in the neighbourhood
    """
    def __init__(self, amstelheage, neighbourhood, houses):
        self.amstelhaege = amstelheage
        self.neighbourhood = neighbourhood
        self.houses = houses
        self.population = []
        self.parents = []
        self.children = []

    def initialize_population(self):
        """
        Generates the initial population by creating individuals with the random_greedy or random
        algorithm
        """
        for i in range(gen.population):
            amstelhaege_copy = deepcopy(self.amstelhaege)

            solution = RandomGreedy(amstelhaege_copy)
            solution.run()

            # create an individual of the population
            chromosome = Chromosome(amstelhaege_copy)
            self.population.append(chromosome)

    def parent_selection(self):
        """
        Randomly selects parents out of the initial population by using their cumaltive fitness
        value
        :return: the list with chromosome objects that together form the initial group of parents
        """
        # calculate the total sum of all fitness values
        self.sum_fitnesses = 0
        for chromosome in self.population:
            self.sum_fitnesses += chromosome.fitness
        
        cum_fitnesses = 0
        # for each chromosome in the population: calculate cumalative fitness values
        for chromosome in self.population:
            cum_fitnesses += chromosome.fitness
            chromosome.cum_fitness = cum_fitnesses
        
        # choose random individuals out of the population
        for chromosome in self.population:
            r = uniform(0, self.sum_fitnesses)
            
            if chromosome.cum_fitness > r:
                self.parents.append(chromosome)
        
        return self.parents
    
    def crossover(self, parents):
        """
        Each parent is used for an crossover with a crossover probability. An house will be randomly placed on one
        of the locations of the parents. If an house can't be placed on either of these locations, the house is 
        randomly placed. 
        :param parents: list of chromosome objects that form the parents (the previous generation)
        """
        for parent in parents:
            # the parent is chosen to reproduce with a crossover probability
            rc = random()
            if rc < probs.crossover:
                # randomly choose the second parent
                parent2 = choice(parents)
                if parent == parent2:
                    continue
                
                # create an empty amstelhaeage area object
                child = Amstelhaege(self.neighbourhood, self.houses)

                for i in range(self.houses):
                    r = random()
                    home = None
                    home1 = parent.amstelhaege.houses[i]
                    home2 = parent2.amstelhaege.houses[i]

                    # with an uniform distribution choose one parent to inherit the location of the house from
                    if r < 0.5:
                        home = parent.amstelhaege.houses[i]
                    else:
                        home = parent2.amstelhaege.houses[i]

                    # if the location is not already occupied, place the house
                    if child.check_location(home.x_left, home.y_bottom, home):
                        child.place_house(home.house_type, home.x_left, home.y_bottom)
                    else:
                        # if the location is occupied, check for the location of the other parent, and otherwise place random
                        if home == home1:
                            if child.check_location(home2.x_left, home2.y_bottom, home2):
                                child.place_house(home2.house_type, home2.x_left, home2.y_bottom)
                            else:
                                random_alg = Random(child)
                                random_alg.place_random(home)
    
                        elif home == home2:
                            if child.check_location(home1.x_left, home1.y_bottom, home1):
                                child.place_house(home1.house_type, home1.x_left, home1.y_bottom)
                            else:
                                random_alg = Random(child)
                                random_alg.place_random(home)
                
                # append the child to the list if all the houses are placed
                child.get_free_space()
                child.calculate_price()
                child = Chromosome(child)
                self.children.append(child)

            
    def survivor_selection(self, parents):
        """
        Mutates the children and forms the new generation by selecting the individuals with the 
        best fitness value out of the group of parents and children combined.
        :parents: list of chromosome objects that form the parents (the previous generation)
        :return: the new generation (survivors), a list of chromosome objects with the best fitness
        """
        self.crossover(parents)
        number_of_chromosomes = len(parents)

        # mutate the children
        for child in self.children:
            child.mutate()
        
        # create a large group including the parents and children and sort this group
        parents += self.children
        parents.sort(reverse=True, key=lambda x: x.fitness)

        # create a list of survivors that is as large as the initial group of parents
        self.survivors = []
        for i in range(number_of_chromosomes):
            self.survivors.append(parents[i])
        
        return self.survivors
        
    def get_average(self, generation):
        """
        Calculates the average fitness value of a generation
        :param generation: a list of chromosome objects that form a generation
        :return: the average fitness value of a generation
        """
        worth = []
        for individual in generation:
            worth.append(individual.fitness)
        
        return sum(worth)/len(generation)

    def run(self):  
        """
        Runs the genetic algorithm
        :return: the amstelhaege area of the best individual/chromosome of the last generation
        """
        print("start")
        # generate the initial population and select parents
        self.initialize_population()
        parents = self.parent_selection()

        counter = 0
        average = self.get_average(parents)

        # terminate when the average of a generation doesn't increase anymore
        while counter < gen.termination:

            # create a new generation
            survivors = self.survivor_selection(parents)
            
            if self.get_average(survivors) <= average:
                counter += 1
            else:
                average = self.get_average(survivors)
                counter = 0
            
            parents = survivors
            best_individual = parents[0]
            best_individual.amstelhaege.get_free_space()
            best_individual.amstelhaege.calculate_price()
        
        # get the individual with the highest fitness value
        best_individual = parents[0]
        best_individual.amstelhaege.get_free_space()
        best_individual.amstelhaege.calculate_price()
        print(f"{best_individual.amstelhaege.price}")
        return best_individual.amstelhaege