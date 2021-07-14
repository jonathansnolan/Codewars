# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 20:19:18 2020

@author: Emily
"""
#######################################
# SOLUTION
#######################################

def fake_bin(s):
    return ''.join('0' if int(c) < 5 else '1' for c in s)