# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 15:15:31 2020

@author: Emily
"""
########################################
# QUESTION
########################################

# This time no story, no theory. The examples below show you how to write function accum:

# Examples:

# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"

###################################
# SOLUTION
###################################

def accum(s):
    x = list(s)
    i = []
    for k in list(range(0,len(x))):
        i.append(s[k]*(k+1))
    j = ''
    for k in list(range(0,len(i))):
        j += i[k].title() + "-"
    n = len(j)
    j = j[0:(n-1)]
    return j
    # your code

print(accum("adafdaff"))