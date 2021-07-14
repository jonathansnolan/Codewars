# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 15:19:16 2020

@author: Emily
"""
###################################
# QUESTION
###################################

# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Finish the solution so that it returns the sum of all the multiples of 3 or 5 
# below the number passed in.

# Note: If the number is a multiple of both 3 and 5, only count it once. 
# Also, if a number is negative, return 0(for languages that do have them
                  
###################################
# SOLUTION
###################################
                                                                                             
def solution(number):
    if number < 0:
        return 0
    else:
        x = list(range(3,number,3))
        y = list(range(5,number,5))
        z = x + y
        z = list(dict.fromkeys(z))
        ans = sum(z)
        return ans
    

solution(23)