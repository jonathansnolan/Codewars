# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 21:45:02 2020

@author: Emily
"""
########################################
# QUESTION
########################################

# Build Tower
# Build Tower by the following given argument:
# number of floors (integer and always greater than 0).

# Tower block is represented as *

# Python: return a list;
# JavaScript: returns an Array;
# C#: returns a string[];
# PHP: returns an array;
# C++: returns a vector<string>;
# Haskell: returns a [String];
# Ruby: returns an Array;
# Lua: returns a Table;
# Have fun!


###################################
# SOLUTION
###################################

def tower_builder(n_floors):
    
    stars = []
    stars = list(range(1,n_floors*2,2))
    
    tower = []
    
    for k in stars:
        tower.append(("*" * k))
    
    for k in list(range(0, len(tower)-1)):
        tower[k] = " "*int((len(tower[-1])-len(tower[k]))/2) + tower[k] + " "*int((len(tower[-1])-len(tower[k]))/2)
    
    return tower