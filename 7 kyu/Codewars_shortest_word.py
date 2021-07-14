# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 15:24:55 2020

@author: Emily
"""
########################################
# QUESTION
########################################

# Simple, given a string of words, return the length of the shortest word(s).

# String will never be empty and you do not need to account for different data types.

###################################
# SOLUTION
###################################

def find_short(s):
    s = s.split(" ")
    i = []
    for x in s:
        i.append(len(x))
    
    if i == []:
        return 1
    else:
        return min(i)