# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 09:32:00 2020
@author: halle

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""


def prime(input):
    Dict = {input:1}
    for i in range (2,input):
        if 1 in Dict.keys():
            break
        else:    
            while input % i == 0:
                input /= i
                Dict[int(input)]=i
    return Dict

input = 600851475143
Dict = (prime(input))
lst = list(Dict.values())
max_prime = max(lst)

print(Dict)
print(lst)
print(max_prime)
