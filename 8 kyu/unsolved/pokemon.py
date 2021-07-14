# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 18:32:10 2020

@author: Emily
"""

def calculate_damage(your_type, opponent_type, attack, defense):
    if your_type == "fire":
        if opponent_type == "grass":
            eff = 2
        elif opponent_type == "water":
            eff = 0.5
        elif opponent_type == "electric":
            eff = 1
    elif your_type == "grass":
        if opponent_type == "fire":
            eff = 0.5
        elif opponent_type == "electric":
            eff = 1
        elif opponent_type == "water":
            eff = 2
    elif your_type == "water":
        if opponent_type == "fire":
            eff = 2
        elif opponent_type == "grass":
            eff = 0.5
        elif opponent_type == "electric":
            eff = 0.5
    elif your_type == "electric":
        if opponent_type == "grass":
            eff = 1
        elif opponent_type == "water":
            eff = 0.5
        elif opponent_type == "fire":
            eff = 1
    
    z = 50 * (attack / defense) * eff
    return z


#print(calculate_damage("grass", "water", 100, 100))
print(calculate_damage("electric", "fire", 100, 100))