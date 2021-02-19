#!/usr/bin/python3
def power(x,y):
    if  y != 0 :
        return power(y,x%y)
    else:
        return x
print(power(500,100))
        
        
