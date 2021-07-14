# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 19:02:47 2020

@author: Emily
"""

# def add(num1, num2):
#     # just put these initial values down to the length
#     x = len(str(num1))
#     y = len(str(num2))
#     z = 0
    
#     if x >= y :
#         for k in range(0,x): 
#             z = z + int(num1/(10**x)) + int(num2/(10**x))
#     else:
#          for k in range(0,y):
#              z = z + int(num1/(10**y)) + int(num2/(10**y))
#     return z




def add(num1, num2):
    
    # PART 1:
    # Last numbers added together
    
    x = (num1 - (int(num1/10))*10)
    y = (num2 - (int(num2/10))*10)
    if x == 0 and y == 0:
        z = num1 + num2
    elif x == 0:
        z = num1 + y
    elif y == 0:
        z = x + num2
    else:
        z = x + y
#    return z
# Plan is to change this into a string value and add it at the end
        
        
    # PART 2:
    # Last numbers added together
    a = len(str(num1))-1
    b = len(str(num2))-1
   
    c = int(num1/(10**a)) + int(num2/(10**a))   
    f = int(num1/(10**(a-1))) + int(num2/(10**(a-1)))
    return int(str(c)+str(f)+str(z))


print(add(807,337))