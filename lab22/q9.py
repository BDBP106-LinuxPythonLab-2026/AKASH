from inspect import GEN_CLOSED


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

@log_function_call
def gc_content():
    print("DNA Analysis working.....")
    print("Analysis Completed")

analyse_dna('AGGGGCCCCCATTATATATATATAGGGGGGGGGGGTATCCCCCCCCCCCCCCCCCCCCATATAT')
