# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 16:00:31 2020

@author: Emily
"""

########################################
# QUESTION
########################################

# It's the academic year's end, fateful moment of your school report. The averages must be calculated. 
# All the students come to you and entreat you to calculate their average for them. 
# Easy ! You just need to write a script.

# Return the average of the given array rounded down to its nearest integer.

# The array will never be empty.


###################################
# SOLUTION
###################################


def get_average(marks):
    return int(sum(marks)/len(marks))

print(get_average([1,2,3,4,5]))