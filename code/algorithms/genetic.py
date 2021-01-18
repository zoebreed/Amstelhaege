from code.algorithms.random import Random
from copy import deepcopy

# class Genetic():

#     def __init__(self, amstelhaege):
#         self.amstelhaege_copy = deepcopy(amstelheage)
    
#     def generate_population(self):
#         self.population = []
#         for i in range(25):
#             random = Random(self.amstelhaege_copy)
#             random.run(10)
#             self.population.append(random.amstelhaege)

#     def calculate_fitness(self):


#     def run(self):
#         pass

class Chromosome():
    def __init__(self, amstelhaege):
        self.amstelhaege_copy = deepcopy(amstelheage)
    
    def calculate_fitness(self):
        self.worth = self.amstelhaege_copy.calculate_worth()
        self.fitness = self.worth / 1000000
    
    def crossover(self):
        pass

    def mutation(self):
        pass

class Genetic():
    def __init__(self):
        pass 

    def generate_population(self):
        pass

    def parent_selection(self):
        pass 

    def run(self):

    

