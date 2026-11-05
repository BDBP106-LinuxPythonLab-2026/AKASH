import numpy as np


t = np.arange(0, 121, 20)


population = 100 * 2**(t / 20)

print("Time Points:")
print(t)

print("Cell Population:")
print(population)

print("Times larger:",
      population[-1] / population[0])

print("Time points where population > 1000:")
print(t[population > 1000])
