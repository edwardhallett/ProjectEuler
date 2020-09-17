# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 22:35:59 2020

@author: halle
"""

# maths variables (do not change)
i = 1
n = 1
step = 1

# set the number you wish the answer to be evenly divisible up to
upper = 20

# function that checks if "num" is divisible by all numbers from 1 to "high"
def divisible(num,high):
    result = True
    for i in range(1,high+1):
        if num % i != 0:
            result = False
    return result

# script that produces the smallest positive number that is evenly divisible by all of the numbers from 1 to "upper"
# Any "i" for a given "n" must be a multiple of "i" for "n-1"

while True:
    if divisible(i,n) == True:
        if n == upper:
            print(i)
            break
        n += 1
        step = i
    else:
        i += step