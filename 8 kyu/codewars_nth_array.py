# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 16:25:53 2020

@author: Emily
"""
########################################
# QUESTION
########################################

# You are given an array with positive numbers and a number N. 
# You should find the N-th power of the element in the array with the index N. 
# If N is outside of the array, then return -1. 
# Don't forget that the first element has the index 0.

# Let's look at a few examples:

# array = [1, 2, 3, 4] and N = 2, then the result is 3^2 == 9;
# array = [1, 2, 3] and N = 3, but N is outside of the array, so the result is -1.

###################################
# SOLUTION
###################################


#array = [1, 2, 3, 4] 

array = [1, 2]

n = 2

def index(array, n):
    if n in array:
        if len(array) > (n):
            z = array[n]**n
        else:
            return -1
    else:
        return -1
    return z
    
print(index(array, n))