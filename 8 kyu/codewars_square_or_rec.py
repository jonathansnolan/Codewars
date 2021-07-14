# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 12:06:10 2020

@author: Emily
"""
########################################
# QUESTION
########################################

# You are given the length and width of a 4-sided polygon. 
# The polygon can either be a rectangle or a square.
# If it is a square, return its area. 
# If it is a rectangle, return its perimeter.

###################################
# SOLUTION
###################################


def area_or_perimeter(l , w):
    if l == w:
        return l*w
    else:
        return l*2 + w*2
    
print(area_or_perimeter(4, 5))
    # return your answer