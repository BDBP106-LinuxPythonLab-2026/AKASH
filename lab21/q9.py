
import math
def population_growth(initial, rate, time):
    def exponential_growth():
        final = initial + math.exp(rate*time)
        return final
    answer =exponential_growth()
    print(round(answer))


population_growth(50, 0.1, 10)


