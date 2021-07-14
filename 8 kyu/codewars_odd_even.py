# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 11:23:58 2020

@author: Emily
"""

########################################
# QUESTION
########################################

# Create a function (or write a script in Shell) that takes an integer as an argument 
# and returns "Even" for even numbers or "Odd" for odd numbers.

###################################
# SOLUTION
###################################

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"