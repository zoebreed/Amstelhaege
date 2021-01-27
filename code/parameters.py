from collections import namedtuple  

simulatedAnnealing = namedtuple('simulated_annealing', ['Tmax', 'Tmin', 'alpha'])
simAnn = simulatedAnnealing(

    170000,                # Tmax: begin temperature
    1000,                  # Tmin: end temperature
    10                     # alpha: step size
)

geneticAlgorithm = namedtuple('genetic', ['population', 'termination'])
gen = geneticAlgorithm(

    25,                    # population: number of individuals in initial population
    100                    # termination: number of iterations that the average of a population doesn't have to increase
)

probabilities = namedtuple('probability', ['mutation', 'crossover'])
probs = probabilities(

    0.5,                   # mutation: mutation probability
    0.6                    # crossover: crossover probability
)

iterations = namedtuple('iteration', ['hillclimber', 'randomGreedy', ])
iters = iterations(

    1000,                  # hillclimber: iterations
    400                    # randomGreedy: iterations
)


# __________________________ information about each house type is stored below __________________________

houseInformation = namedtuple('houseInformation', ['name', 'type', 'percentage', 'width', 'length', 'increase_value', 'value', 'free_area'])
house1 = houseInformation(

    'eengezinswoning',     # name
    1,                     # type
    0.6,                   # percentage: percentage of total houses
    8,                     # width
    8,                     # length
    0.03,                  # increase_value: percentage per extra meter free area
    285000,                # value: base value of the house
    2                      # free_area: mandatory free area
)
house2 = houseInformation(

    'bungalow',            # name
    2,                     # type
    0.25,                  # percentage: percentage of total houses
    11,                    # width
    7,                     # length
    0.04,                  # increase_value: percentage per extra meter free area
    399000,                # value: base value of the house
    3                      # free_area: mandatory free area
)
house3 = houseInformation(
    
    'maison',              # name
    3,                     # type
    0.15,                  # percentage: percentage of total houses
    12,                    # width
    10,                    # length
    0.06,                  # increase_value: percentage per extra meter free area
    610000,                # value: base value of the house
    6                      # free_area: mandatory free area
)