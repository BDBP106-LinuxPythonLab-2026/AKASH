

def log_function_call(func):
    def wrapper(*args, **kwargs):        #like multiple argument hone wale hai wo use these
        print("Running DNA analysis....")
        result = func(*args, **kwargs)      #parameter we used func in this ans wo apne multiple argument lega
        print("Analysis complete!")
        return result
    return wrapper



@log_function_call
def analyse_dna(s):
     def gc_content():
         G = s.count('G')
         C = s.count('C')
         GC= ((G +C)/len(s) )*100
         print(GC)
         return GC

     result = gc_content()
     # return result   no need of this as it stops the function better not use it after assignment/reference

     if result < 50:
        print("s is AT rich")
     elif result > 50:
        print("s is GC RICH")
     else:
        print("equally present")

analyse_dna('AGGGGCCCCCATTATATATATATAGGGGGGGGGGGTATCCCCCCCCCCCCCCCCCCCCATATAT')
