# (5) Write a decorator measure_time to calculate how long a function takes to run. Use it
# on a function that calculates the factorial of a number. Use a test case of calculating the
# factorial of 50.
import time

def measure_time(func):
    def wrapper(n):
        start = time.time()
        result = func(n)       #unterstand the func(n) logic !
        end = time.time()

        print("Time taken to run:", end - start, "seconds")
        return result

    return wrapper


@measure_time
def factorial(n):
    fact = 1
    for i in range(1, n +1):
        fact *= i
    return fact

factorial(50)    #question asks to check for this so , make sure to call the decorator function and put 50 in it !
