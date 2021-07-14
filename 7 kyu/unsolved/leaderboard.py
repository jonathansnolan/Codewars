# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 17:24:09 2020

@author: Emily
"""

leaderboard = ['John', 'Brian', 'Jim',  'Dave', 'Fred']
changes = ['Dave +1', 'Fred +4', 'Brian -1']

def leaderboard_sort(leaderboard, changes):
    x = []
    for k in changes:
        x.append(k[-2:])
    
    print(x)
    
leaderboard_sort(leaderboard, changes)