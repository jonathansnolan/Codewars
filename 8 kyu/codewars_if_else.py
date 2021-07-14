# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 16:20:48 2020

@author: Emily
"""
########################################
# QUESTION
########################################

# If/else syntax debug
# While making a game, your partner, Greg, decided to create a function to check if the user is still alive called checkAlive/CheckAlive/check_alive. Unfortunately, Greg made some errors while creating the function.

# checkAlive/CheckAlive/check_alive should return true if the player's health is greater than 0 or false if it is 0 or below.

# The function receives one parameter health which will always be a whole number between -10 and 10.

###################################
# SOLUTION
###################################

def check_alive(health):
    if health > 0:
        return True
    else:
        return False