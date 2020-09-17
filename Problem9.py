# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 22:40:35 2020

@author: halle
"""

m=2
n=1
summ = 0

while True:
    a = m**2 - n**2
    b = 2*n*m
    c = n**2 + m**2
    summ = 2*(m**2) + 2*n*m
    if summ == 1000:
        print([a,b,c])
        print(a*b*c)
        break
    elif summ >1000:
        n += 1
        m = n + 1
    else:
        m += 1