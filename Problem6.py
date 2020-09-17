# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 22:37:12 2020

@author: halle
"""

sum_o_sq = 0
summ = 0
sq_o_sum = 0

for i in range(101):
    sum_o_sq += i**2
    summ += i
sq_o_sum = summ**2
dif = sq_o_sum - sum_o_sq

print(dif)