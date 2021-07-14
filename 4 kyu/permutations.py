# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 13:56:55 2020

@author: Emily
"""

import itertools

def permutations(string):
    x = list(string)
    y = list(itertools.permutations(x, len(x)))
    
    i = []
    
    for k in y:
        m = ""
        for u in k:
            m += u
        i.append(m)
    return list(dict.fromkeys(i))