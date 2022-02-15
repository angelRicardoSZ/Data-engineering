from cmath import sqrt


import math as mt
def run():
    #my_dict = {}
    
    #for i in range(1,101):
    #    if i % 3 != 0:
    #        my_dict[i]=i**3
        
    #print(my_dict)
    
    my_dict = {i:i**3 for i in range(1,101) if i % 3!=0}
    my_dict = {i:round(mt.sqrt(i),2) for i in range(1,1000) if i % 3!=0}
    print(my_dict)
    
    
if __name__=="__main__":
    run()
    