# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 21:06:06 2020

@author: Emily
"""
########################################
# QUESTION
########################################

# Sum Array
# Write a method sum (sum_array in python, sumarray in julia, SumArray in C#) 
# that takes an array of numbers and returns the sum of the numbers. 
# These may be integers or decimals for Ruby and any instance of Num for Haskell. #
# The numbers can also be negative. If the array does not contain any numbers then you should return 0.
                
###################################
# SOLUTION
###################################
    
def sum_array(a):
    x = len(a)
    z = 0
    for k in range(0,(x)):
        z = z + a[k]
    if a == []:
        return 0
    else:
        return z