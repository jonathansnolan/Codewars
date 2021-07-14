# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 11:11:17 2020

@author: Emily
"""
########################################
# QUESTION
########################################

# Define a method hello that returns "Hello, Name!" to a given name, or says Hello, World! 
# if name is not given (or passed as an empty String).

# Assuming that name is a String and it checks for user typos to return a name 
# with a first capital letter (Xxxx).

# Examples:

# hello "john"   => "Hello, John!"
# hello "aliCE"  => "Hello, Alice!"
# hello          => "Hello, World!" # name not given
# hello ''       => "Hello, World!" # name is an empty String


###################################
# SOLUTION
###################################

def hello(name = ''):
    if name:
        x = "Hello, " + str(name) + "!"
    else:
        if name == " ":
            x = "Hello, World!"
        else:
            x = "Hello, World!"
    return(x.title())



print(hello("jonATHaN"))

print(hello("aLICe"))
print(hello())

        