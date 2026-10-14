# (4) Write a decorato called check_positive that checks whether the argument passed to
# a function is positive. If it is positive, execute the function; otherwise, print
# "Number must be positive".


def check_decorator(func):
    def wrapper(number):
        if number > 0:
            func(number)
            print("Argument is Positive")
        else:
            print("Number must be Positive")
    return wrapper



@check_decorator
def check_positive(number):
    print("Checking positive...")


check_positive(5)
check_positive(-2)
