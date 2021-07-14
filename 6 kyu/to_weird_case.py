# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 23:01:57 2020

@author: Emily
"""

def to_weird_case(string):
    x = string.split()
    
    whole = ""
    for k in x:
        whole += k
    
    i = ""    
    for q in list(range(0,len(whole))):
            if q % 2 == 0:
                i += whole[q].upper()
            else:
                i += whole[q].lower()
    
    loca = []
    for k in list(range(0,len(string))):
        if string[k] == " ":
            loca.append(k)
    if loca == []:
        return i
    else:
        for n in loca:
            i = i[:n] + " " + i[n:]
        
        return i