# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 17:52:09 2020

@author: Emily
"""


###################################
# SOLUTION
###################################

def to_alternating_case(string):
    x = list(string)
    c = ""
    for k in x:
        if k == k.upper():
            c += k.lower()
        elif k == k.lower():
            c += k.upper()
        else:
            c += k
    return c    