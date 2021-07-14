# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 11:25:16 2020

@author: Emily
"""

def am_i_wilson(n):
    if n <= 1 and n >= 0:
       return False
    else:
       f = 1
       for k in range(1,n):
           f = f*k

       z = ((f) + 1) / (n * n)
       if (z-int(z)) == 0:
           return True
       else:
           return False

    
print(am_i_wilson(5))