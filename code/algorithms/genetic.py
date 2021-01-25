from code.algorithms.random import Random
from code.algorithms.random_greedy import Random_greedy
from code.classes.Amstelhaege import Amstelhaege
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

    def mutate(self):
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
                else:
                    house.move(house_x, house_y)
                    house2.move(house2_x, house2_y)
                
                self.amstelhaege.get_free_space()
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
                    else:
                        counter += 1
            
                self.amstelhaege.get_free_space()
                self.worth = self.amstelhaege.calculate_worth()

class Genetic():
    def __init__(self, amstelheage, neighbourhood, houses):
        self.amstelhaege = amstelheage
        self.neighbourhood = neighbourhood
        self.houses = houses
        self.population = []
        self.parents = []


    def initialize_population(self):
        for i in range(25):
            print(i)
            amstelhaege_copy = deepcopy(self.amstelhaege)
            randomsol = Random(amstelhaege_copy)
            randomsol.run()
            chromosome = Chromosome(amstelhaege_copy)
            self.population.append(chromosome)

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
            
            if chromosome.cum_fitness > r:
                self.parents.append(chromosome)
        
        return self.parents
    
    def crossover(self, parents):
        self.children = []
        for parent in parents:
            rc = random.random()
            if rc < 0.7:
                parent2 = random.choice(parents)
                if parent == parent2:
                    continue

                child = Amstelhaege(self.neighbourhood, self.houses)

                for i in range(self.houses):
                    r = random.random()
                    home = None
                    home1 = parent.amstelhaege.houses[i]
                    home2 = parent2.amstelhaege.houses[i]
                    if r < 0.5:
                        home = parent.amstelhaege.houses[i]
                    else:
                        home = parent2.amstelhaege.houses[i]

                    if child.check_location(home.x_left, home.y_bottom, home.width, home.length, home.free_area):
                        child.place_house(home.house_type, home.x_left, home.y_bottom)
                    else:
                        if home == home1:
                            if child.check_location(home2.x_left, home2.y_bottom, home2.width, home2.length, home2.free_area):
                                child.place_house(home2.house_type, home2.x_left, home2.y_bottom)
                            else:
                                placed = False
                                while placed == False:
                                    x = random.randrange(child.width)
                                    y = random.randrange(child.length)
                                    if child.check_location(x, y, home.width, home.length, home.free_area):
                                        child.place_house(home.house_type, x, y)
                                        placed = True
                        elif home == home2:
                            if child.check_location(home1.x_left, home1.y_bottom, home1.width, home1.length, home1.free_area):
                                child.place_house(home1.house_type, home1.x_left, home1.y_bottom)
                            else:
                                placed = False
                                while placed == False:
                                    x = random.randrange(child.width)
                                    y = random.randrange(child.length)
                                    if child.check_location(x, y, home.width, home.length, home.free_area):
                                        child.place_house(home.house_type, x, y)
                                        placed = True
                    
                child.get_free_space()
                child.calculate_worth()
                # print(f"parent1 {parent.amstelhaege.price} parent2 {parent2.amstelhaege.price} child {child.price}")
                child = Chromosome(child)
                self.children.append(child)

            
    def survivor_selection(self, parents):
        self.crossover(parents)
        number_of_chromosomes = len(parents)
        for child in self.children:
            child.mutate()
        
        parents += self.children
        parents.sort(reverse=True, key=lambda x: x.worth)

        self.survivors = []
        for i in range(number_of_chromosomes):
            self.survivors.append(parents[i])
        
        return self.survivors
        
    def get_average(self, generation):
        worth = []
        for individual in generation:
            worth.append(individual.worth)
        
        return sum(worth)/len(generation)

    def run(self):  
        self.initialize_population()
        parents = self.parent_selection()
        counter = 0
        averages = [self.get_average(parents)]
        while counter < 500:

            # mutate and find survivors
            survivors = self.survivor_selection(parents)
            
            if self.get_average(survivors) <= max(averages):
                counter += 1
            else:
                counter = 0
            
            averages.append(self.get_average(survivors))
            parents = survivors
            # best_individual = parents[0]
            # best_individual.amstelhaege.get_free_space()
            # best_individual.amstelhaege.calculate_worth()
            # print(best_individual.amstelhaege.price)
        
        best_individual = parents[0]
        best_individual.amstelhaege.get_free_space()
        best_individual.amstelhaege.calculate_worth()
        return best_individual.amstelhaege

from visualise import visualise
# from code.classes.Amstelhaege import Amstelhaege
# from copy import deepcopy
# import random
# from code.algorithms.random import Random
# from code.algorithms.random_greedy import Random_greedy

# amstelhaege1 = Amstelhaege(1, 20)
# map1 = deepcopy(amstelhaege1)
# random1 = Random_greedy(map1)
# random1.run()
# map1.get_free_space()
# map1.calculate_worth()
# # visualising the results
# visualise(map1.waters, map1.houses, map1.price)
# print(f"Map1 {map1.price}")

# amstelheage2 = Amstelhaege(1, 20)
# map2 = deepcopy(amstelheage2)
# random2 = Random_greedy(map2)
# random2.run()
# map2.get_free_space()
# map2.calculate_worth()
# # visualising the results
# visualise(map2.waters, map2.houses, map2.price)
# print(f"Map2 {map2.price}")

# amstelhaege = Amstelhaege(1, 20)

# for i in range(20):
#     r = random.random()
#     home = None
#     home1 = map1.houses[i]
#     home2 = map2.houses[i]
#     if r < 0.5:
#         home = map1.houses[i]
#     else:
#         home = map2.houses[i]
#     if amstelhaege.check_location(home.x_left, home.y_bottom, home.width, home.length, home.free_area):
#         amstelhaege.place_house(home.house_type, home.x_left, home.y_bottom)
#     else:
#         if home == home1:
#             if amstelhaege.check_location(home2.x_left, home2.y_bottom, home2.width, home2.length, home2.free_area):
#                 amstelhaege.place_house(home2.house_type, home2.x_left, home2.y_bottom)
#             else:
#                 placed = False
#                 while placed == False:
#                     x = random.randrange(amstelhaege.width)
#                     y = random.randrange(amstelhaege.length)
#                     if amstelhaege.check_location(x, y, home.width, home.length, home.free_area):
#                         amstelhaege.place_house(home.house_type, x, y)
#                         placed = True
#         if home == home2:
#             if amstelhaege.check_location(home1.x_left, home1.y_bottom, home1.width, home1.length, home1.free_area):
#                 amstelhaege.place_house(home1.house_type, home1.x_left, home1.y_bottom)
#             else:
#                 placed = False
#                 while placed == False:
#                     x = random.randrange(amstelhaege.width)
#                     y = random.randrange(amstelhaege.length)
#                     if amstelhaege.check_location(x, y, home.width, home.length, home.free_area):
#                         amstelhaege.place_house(home.house_type, x, y)
#                         placed = True

# amstelhaege.get_free_space()
# amstelhaege.calculate_worth()

# # visualising the results
# visualise(amstelhaege.waters, amstelhaege.houses, amstelhaege.price)
# print(f"amstelhaege {amstelhaege.price}")