# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 22:37:52 2020

@author: halle
"""

ans_loc = 10001
primes = []
j = 2

def eq_prime(num):
    result = True
    for i in range (2,int(num/2)+1):
        if num % i == 0:
            result = False
            break
    return result

while len(primes) < ans_loc:
    if eq_prime(j) == True:
        primes.append(j)
    j += 1
 
print(primes[ans_loc-1])