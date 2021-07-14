# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 20:52:50 2020

@author: Emily
"""

########################################
# QUESTION
########################################

# Given a month as an integer from 1 to 12, 
# return to which quarter of the year it belongs as an integer number.

# For example: month 2 (February), is part of the first quarter; 
# month 6 (June), is part of the second quarter; and month 11 (November), is part of the fourth quarter.


###################################
# SOLUTION
###################################

def quarter_of(month):
    if month >= 0 and month <=3:
        return 1
    else:
        if month >= 4 and month <= 6:
            return 2
        else:
            if month >= 7 and month <= 9:
                return 3
            else:
                return 4