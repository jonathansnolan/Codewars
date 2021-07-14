# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 15:38:59 2020

@author: Emily
"""

y = "whats happening jonathan. are you good :). lower. case. test"

def cap(n):
    return ". ".join(k.capitalize() for k in y.split(". "))

print(cap(y))                     