# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 20:18:36 2020

@author: Emily
"""

def bouncing_ball(h, bounce, window):
    
    if window > h and h < 0 and bounce > 0 and bounce < 1:
        return -1
    
    count = 1
    x = h*bounce
    
    while x > window:
        x = x*bounce
        count += 2
    # your code
    return count


print(bouncing_ball(50, 0.75, 1.5))