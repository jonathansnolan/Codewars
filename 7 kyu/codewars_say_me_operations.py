# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 16:30:30 2020

@author: Emily
"""

########################################
# QUESTION
########################################


# You have a string with N numbers, starting with the third number each number is the result of an operation performed using the previous two numbers.

# Write a function which returns a string of the operations in order and separated by a comma and a space (e.g. "subtraction, subtraction, addition").

# Available operations are:

# 1) addition
# 2) subtraction
# 3) multiplication
# 4) division
# Example: for string "9 4 5 20 25"

# Your function must return:

# "subtraction, multiplication, addition"

# Because:

# 9 - 4 = 5 - subtraction,
# 4 * 5 = 20 - multiplication,
# 5 + 20 = 25 - addition.
# All input data is valid.
# Number of numbers in input string >= 3.
# For a case like "2 2 4" - when multiple variants are possible - choose the first possible operation from the list.
# Integer division should be used.

###################################
# SOLUTION
###################################

def sayMeOperations(stringNumbers):
    
    x = stringNumbers.split()

    
    z = []
    for k in x:
        z.append(int(k))
    
    p = []
    for k in list(range(2,len(z))):
        if z[k] == z[k-2] + z[k-1]:
            p.append("addition")
        else:
            if z[k] == z[k-2] - z[k-1]:
                p.append("subtraction")
            else:
                if z[k] == z[k-2] * z[k-1]:
                    p.append("multiplication")
                else:
                    if z[k] == z[k-2] // (z[k-1]):
                        p.append("division")
                    else:
                        if z[k] == -(z[k-2] / (z[k-1])):
                            p.append("division")
    print(p)
    n = ''        
    for k in p:
        n += k +', '
    n = n[0:-2]
    return n    
    
sayMeOperations("1 2 3 5 8")         
sayMeOperations("1 2 3 5 8")         

sayMeOperations("9 4 5 20 25")   