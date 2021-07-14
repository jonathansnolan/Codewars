# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 16:09:51 2020

@author: Emily
"""

########################################
# QUESTION
########################################

# Given an array of integers, find the one that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.

###################################
# SOLUTION
###################################

def find_it(seq):
    x = list(dict.fromkeys(seq))
    
    u = []
    for w in x:
        i = 0
        for k in seq:
            if k == w:
                i += 1
        u.append(i)        
    
    for k in list(range(0,len(u))):
        if u[k] % 2 != 0:
            return x[k]