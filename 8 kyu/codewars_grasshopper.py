# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 16:55:36 2020

@author: Emily
"""

def convert_to_celsius(temperature):
    celsius = (temperature - 32) * (5/9)
    return celsius

def weather_info(temp):
    c = convert_to_celsius(temp)
    if (c > 0):
        return (str(c) + " is freezing temperature")
    else:
        return (str(c) + " is above freezing temperature")
    
print(weather_info(50))