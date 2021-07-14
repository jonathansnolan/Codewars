# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 10:46:50 2020

@author: Emily
"""
###################################
# QUESTION
###################################

# Triple Trouble
# Create a function that will return a string that combines 
# all of the letters of the three inputed strings in groups. 
# Taking the first letter of all of the inputs and grouping 
# them next to each other. Do this for every letter, see example below!

# E.g. Input: "aa", "bb" , "cc" => Output: "abcabc"

# Note: You can expect all of the inputs to be the same length.

###################################
# SOLUTION
###################################

def triple_trouble(one, two, three):
    x = [one, two, three]
    y = max(x, key=len)
    z = len(y)
    a = ''
    for k in range(0,z):
        a += x[0][k] + x[1][k] + x[2][k]
    return a