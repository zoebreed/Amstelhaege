from collections import namedtuple  


simulatedAnnealing = namedtuple('simulated_annealing', ['Tmax', 'Tmin', 'alpha'])
simAnn = simulatedAnnealing(

    170000,                # Tmax: begin temperature
    1000,                  # Tmin: end temperature
    10                     # alpha: step size
)

iterations = namedtuple('iteration', ['hillclimber', 'randomGreedy', ])
iters = iterations(

    1000,                  # hillclimber: iterations
    400                    # randomGreedy: iterations
)

houseInformation = namedtuple('houseInformation', ['name', 'width', 'length', 'increase_value', 'value', 'free_area'])
house1 = houseInformation(

    'eengezinswoning',     # name
    8,                     # width
    8,                     # length
    0.03,                  # increase_value: percentage per extra meter free area
    285000,                # value: base value of the house
    2                      # free_area: mandatory free area
)
house2 = houseInformation(

    'bungalow',            # name
    11,                    # width
    7,                     # length
    0.04,                  # increase_value: percentage per extra meter free area
    399000,                # value: base value of the house
    3                      # free_area: mandatory free area
)
house3 = houseInformation(
    
    'maison',              # name
    12,                    # width
    10,                    # length
    0.06,                  # increase_value: percentage per extra meter free area
    610000,                # value: base value of the house
    6                      # free_area: mandatory free area
)

