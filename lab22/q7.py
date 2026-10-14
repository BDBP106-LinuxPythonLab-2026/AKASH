
import math
import time

# Decorator to measure execution time
def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Time taken to run:", end - start, "seconds")
        return result

    return wrapper


@measure_time
def population_growth(initial, rate, time):
    def exponential_growth():
        final = initial + math.exp(rate*time)
        return final

    for i in range(1000000):
        answer = exponential_growth()

    print("Population after time T is:", round(answer))
    return answer

population_growth(50, 0.1, 10)
