# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 10:10:54 2020

@author: Emily
"""



def subtract_sum(number):
    x = len(str(number))
    n = 0
    for k in range(0,x):
        j = str(number)
        n += int(j[k])
    new = number - n
    if new >= 100:
        x = len(str(new))
        m = 0
        for k in range(0,x):
            j = str(new)
            m += int(j[k])
            new_1 = new - m
        return new_1
    else:
        return new
        
print(subtract_sum(325))