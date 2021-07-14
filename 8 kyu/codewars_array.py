# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 15:21:07 2020

@author: Emily
"""

########################################
# QUESTION
########################################

# We want an array, but not just any old array, an array with contents!

# Write a function that produces an array with the numbers 0 to N-1 in it.

# For example, the following code will result in an array containing the numbers 0 to 4:

###################################
# SOLUTION
###################################

def arr(n= ''):
    if n:
        z = list(range(0, n))
    else:
        z = []
    return z
    
print(arr())