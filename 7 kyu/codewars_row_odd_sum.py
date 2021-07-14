# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 14:14:17 2020

@author: Emily
"""

###################################
# QUESTION
###################################

# Given the triangle of consecutive odd numbers:

#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29

# Calculate the row sums of this triangle from the row index (starting at index 1) e.g.:

# row_sum_odd_numbers(1); # 1
# row_sum_odd_numbers(2); # 3 + 5 = 8


###################################
# SOLUTION
###################################

def row_sum_odd_numbers(n):
    count = sum(list(range(0,n+1)))
    end = count*2+1
    odd = list(range(1,end,2))
    ran = count - n
    
    row = odd[ran:]
    return (sum(row))
    
row_sum_odd_numbers(6)