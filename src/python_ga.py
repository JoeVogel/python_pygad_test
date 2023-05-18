import numpy

variables_number = 4           # number of variables

# Upper and lower limits D,Z,AEdAO,PdD,
upper_limit = [0.8, 7, 1.05, 1.4]
lower_limit = [0.5, 2, 0.30, 0.5]

# Method Differential Evolution
population_size = 30   # population size
generations = 30       # Number of iterations (generations)
crossover_factor = 0.5 # factor that defines the crossover (0.5 < CR < 1)
mutation_factor = 0.8  # weight function that defines the mutation (0.5 < F < 1).

xpo = numpy.zeros((population_size,variables_number))
VFi = numpy.zeros((population_size,4))
VFpo = numpy.zeros((population_size,4))