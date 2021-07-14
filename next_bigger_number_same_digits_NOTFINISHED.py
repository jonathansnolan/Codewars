# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 16:19:08 2020

@author: Emily
"""

from itertools import product 

def next_bigger(n):
    x = list(str(n))
    i = []
    for k in x:
        i.append(int(k))
    perm = permutations(i, len(x), )
    
    
    
    for k in list(range(0,len(p))):
        if n == p[k]:
            return int(p[k+1])
        
print(next_bigger(12345313))