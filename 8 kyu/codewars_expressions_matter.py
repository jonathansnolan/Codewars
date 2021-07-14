# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 16:01:06 2020

@author: Emily
"""

def expression_matter(a, b, c):
    x = a + b + c
    y = (a + b) * c
    z = a * (b + c)
    w = a * b * c
    
    lis = [x, y, z, w]
    ans = max(lis)
    return ans # highest achievable result

print(expression_matter(2, 1, 2))