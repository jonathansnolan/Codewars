# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 19:07:16 2020

@author: Emily
"""

########################################
# QUESTION
########################################

# Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

# ! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)

# ##Examples :

# iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even

# iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd


###################################
# SOLUTION
###################################

def iq_test(numbers):
    numbers = numbers.split(" ")
    x = list(numbers)
    
    odd_count = 0
    odd = [] 
    even_count = 0
    even = []
    
    for k in list(range(0,len(x))):
        if int(x[k]) % 2 == 0:
            even_count += 1
            even.append(k)
        elif int(x[k]) % 2 != 0:
            odd_count += 1
            odd.append(k)
    
    if even_count > odd_count:
        return odd[0]+1
    if even_count < odd_count:
        return even[0]+1
    
print(iq_test("1 2 2"))