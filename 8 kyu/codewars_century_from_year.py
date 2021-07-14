# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 09:56:19 2020

@author: Emily
"""
########################################
# QUESTION
########################################

# Introduction
# The first century spans from the year 1 up to and 
# including the year 100, The second - from the year 101 up to 
# and including the year 200, etc.

# Task :
# Given a year, return the century it is in.

# Input , Output Examples ::
# centuryFromYear(1705)  returns (18)
# centuryFromYear(1900)  returns (19)
# centuryFromYear(1601)  returns (17)
# centuryFromYear(2000)  returns (20)

###################################
# SOLUTION
###################################

def century(year):
    if year >= 0 and year <= 100:
        return 1
    else:
        if year % 100 == 0:
            return year/100
        else:
            return int(year/100 +1)