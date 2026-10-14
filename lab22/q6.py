


import math
def population_growth(initial, rate, time):
    def exponential_growth():
        final = initial + math.exp(rate*time)
        return final #so that final is refrenced to the inner function , when it will be call ho jaayega
    answer =exponential_growth()      #call the inner function kyuki solve to bechaara wahi ho rha hai bro
    print(round(answer))              #print me round you have to add ,
    return answer                     #even if you dont do it its fine so yeah like its for saving/refrences
# last 3 lines happening in outer function make sure you kn ow that
population_growth(50, 0.1, 10)    #this is to call the function so make sure you remember to use it nicely.



