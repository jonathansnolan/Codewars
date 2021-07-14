# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 14:53:25 2020

@author: Emily
"""
########################################
# QUESTION
########################################

# In this Kata, we are going to reverse a string while maintaining the spaces (if any) in their original place.

# For example:

# solve("our code") = "edo cruo"
# -- Normal reversal without spaces is "edocruo". 
# -- However, there is a space at index 3, so the string becomes "edo cruo"

# solve("your code rocks") = "skco redo cruoy". 
# solve("codewars") = "srawedoc"
# More examples in the test cases. All input will be lower case letters and in some cases spaces.

# Good luck!

# Please also try:

# Simple time difference

# Simple remove duplicates

###################################
# SOLUTION
###################################

def solve(s):
    x = []
    for k in list(range(0,len(s))):
        if s[k] == " ":
            x.append(k)
    
    y = s.split()
    y = y[::-1]
    
    z = []
    for k in y:
        z.append(k[::-1])
    
    y = []
    for k in z:
        y+=(list(k))
    
    
    for k in x:
        y.insert(k, " ")
        
    j = ""
    for k in y:
        j += k
    
    

        
    return j