# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 14:36:47 2020

@author: Emily
"""

###################################
# SOLUTION
###################################

def add(num1, num2):
    x = str(num1)
    y = str(num2)
    x = list(x)
    y = list(y)
    x1 = x
    y1 = y
    
    x = x[::-1]
    y = y[::-1]
    
    
    a = len(x)
    b = len(y)
    j = min([a,b])
    m = max([a,b])
    
    z = []
    print(list(range(0, j)))
    for k in list(range(0, j)):
        z.append(str(int(x[k]) + int(y[k])))
    
    n = m - j
    ACC = list(range(0, n))
    last = []
    if a>b:
        for k in ACC[::-1]:
            last.append(x1[k])
        z = z+last
        z = z[::-1]
    else:
        for k in ACC[::-1]:
            last.append(y1[k])
        z = z+last
        z = z[::-1]
    
    b = ''
    for k in z:
        b += k
    return int(b)

print(add(122,81))
    
# 1103
add(57589,5935999)