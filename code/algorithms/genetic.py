from code.algorithms.random import Random
from code.algorithms.random_greedy import Random_greedy
from copy import deepcopy
import random

class Chromosome():
    def __init__(self, amstelhaege):
        self.amstelhaege = amstelhaege
        self.cum_fitness = None
        self.worth = self.amstelhaege.calculate_worth()
        self.calculate_fitness()
    
    def calculate_fitness(self):
        self.fitness = self.worth / 1000000
    
    # def crossover(self):
        #TODO: toepasbaar op onze case? 

    def mutate(self):
        #TODO: how are the mutation probabilities found?
        self.swap_houses()
        self.random_coordinates()

        self.calculate_fitness()
    
    def swap_houses(self):
        for house in self.amstelhaege.houses:
            r = random.random()

            if r < 0.2:
                house2 = random.choice(self.amstelhaege.houses)
                if house == house2:
                    continue
                
                house_x = house.x_left
                house_y = house.y_bottom

                house2_x = house2.x_left
                house2_y = house2.y_bottom

                house.move(-100, -100)
                house2.move(-200, -200)

                if self.amstelhaege.check_location(house_x, house_y, house2.width, house2.length, house2.free_area) and self.amstelhaege.check_location(house2_x, house2_y, house.width, house.length, house.free_area):
                    house.move(house2_x, house2_y)
                    house2.move(house_x, house_y)
                    #print(f"house {house.id} and house {house2.id} are swapped")
                else:
                    house.move(house_x, house_y)
                    house2.move(house2_x, house2_y)
                
                self.amstelhaege.get_free_space()
                # self.amstelhaege.calculate_worth()
                self.worth = self.amstelhaege.calculate_worth()

    def random_coordinates(self):
        for house in self.amstelhaege.houses:
            initial_x = house.x_left
            initial_y = house.y_bottom
            r = random.random()
            if r < 0.2:
                counter = 0
                while counter < 500:
                    x = random.randrange(self.amstelhaege.width)
                    y = random.randrange(self.amstelhaege.length)

                    if self.amstelhaege.check_location(x, y, house.width, house.length, house.free_area):
                        house.move(x, y)
                        counter = 500
                        #print(f"house {house.id} is moved")
                    else:
                        counter += 1
            
                self.amstelhaege.get_free_space()
                self.amstelhaege.calculate_worth()
                self.worth = self.amstelhaege.calculate_worth()

class Genetic():
    def __init__(self, amstelheage):
        self.amstelhaege = amstelheage
        self.population = []
        self.parents = []
        self.survivors = []
        # self.algorithm = algorithm


    def initialize_population(self):
        # print("start creating population")
        for i in range(25):
            print(i)
            amstelhaege_copy = deepcopy(self.amstelhaege)
            # if self.algorithm == 'greedy':
            #     randomsol = Random_greedy(amstelhaege_copy, random=False)
            # else:
            randomsol = Random_greedy(amstelhaege_copy, random=False)
            randomsol.run()
            chromosome = Chromosome(amstelhaege_copy)
            self.population.append(chromosome)
            # print(chromosome)

    def parent_selection(self):
        self.sum_fitnesses = 0
        for chromosome in self.population:
            self.sum_fitnesses += chromosome.fitness

        cum_fitnesses = 0
        for chromosome in self.population:
            cum_fitnesses += chromosome.fitness
            chromosome.cum_fitness = cum_fitnesses
        
        for chromosome in self.population:
            r = random.uniform(0, self.sum_fitnesses)
            # print(f"r{r} fitness{chromosome.cum_fitness}")
            
            if chromosome.cum_fitness > r:
                self.parents.append(chromosome)
        
        # for parent in self.parents:
        #     print(parent.worth)
        
        # print(f"The number of parents is {len(self.parents)}")
        return self.parents
            
    def survivor_selection(self, parents):
        parents_copy = deepcopy(parents)
        number_of_chromosomes = len(parents)
        for chromosome in parents_copy:
            chromosome.mutate()
            # print(chromosome.worth)
        
        parents += parents_copy 
        # for parent in parents:
        #     print(parent.worth)
        parents.sort(reverse=True, key=lambda x: x.worth)

        self.survivors = []
        for i in range(number_of_chromosomes):
            self.survivors.append(parents[i])
        
        return self.survivors
        
    def get_average(self, population):
        worth = []
        for individual in population:
            worth.append(individual.worth)
        
        return sum(worth)/len(population)

    def run(self):  
        self.initialize_population()
        parents = self.parent_selection()
        counter = 0
        averages = [self.get_average(parents)]
        while counter < 30:
            # print(f"counter {counter}")
            # mutate and find survivors
            survivors = self.survivor_selection(parents)
            
            if self.get_average(survivors) <= max(averages):
                counter += 1
            else:
                counter = 0
            
            averages.append(self.get_average(survivors))
            parents = survivors
            #print(len(parents))
            best_individual = parents[0]
            #print(best_individual.amstelhaege.price)
            # print(f"worth of best individual is {best_individual.worth}")
        
        #TODO: parents is already sorted
        #print(f"worth of best individual is {best_individual.worth}")
        best_individual = parents[0]
        best_individual.amstelhaege.get_free_space()
        best_individual.amstelhaege.calculate_worth()
        return best_individual.amstelhaege

