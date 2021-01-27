#!/usr/bin/python3
def power(x):
    if x <= 2:
        return 1
    if  x > 2:
        return power(x-1)+power(x-2)

