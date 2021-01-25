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


