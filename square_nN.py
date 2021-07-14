# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 12:23:02 2020

@author: Emily
"""
########################################
# QUESTION
########################################

# In this Kata, you will be given a number n (n > 0) and your task will
#  be to return the smallest square number N (N > 0) 
# such that n + N is also a perfect square. 

# If there is no answer, return -1 (nil in Clojure, Nothing in Haskell, None in Rust).

# solve(13) = 36
# because 36 is the smallest perfect square 
# that can be added to 13 to form a perfect square => 13 + 36 = 49

# solve(3) = 1 # 3 + 1 = 4, a perfect square
# solve(12) = 4 # 12 + 4 = 16, a perfect square
# solve(9) = 16 
# solve(4) = -1

###################################
# SOLUTION
###################################

# numbers = list(range(1,20))
# x = []
# for k in numbers:
#     x.append(k**2)

# def solve(n):
    
    
#     closest = n**0.5
#     below = (int(closest))
#     above = below + 1
    
#     if n >= 1000:
#         z = list((range((below-10)**2 ,(above+10)**2)))
#     else:
#         z = list((range(0,n+10)))
    
#     x = []
#     for k in z:
#         x.append(k**2)
#     j = x
    
#     y = 0
#     for k in x:
#         for u in j:
#             if k + n == u:
#                 y += k
    
#     if y == 0:
#         return -1
#     else:
#         return y
            
def solve(n):
    numbers = list(range(1,100000))
    x = []
    for k in numbers:
        x.append(k**2)
    
    j = 0
    for k in x:
        if k - n >= 0 and ((k - n)**0.5) == int((k - n)**0.5):
            j += k
    
    return (j-n)    

print(solve(12))


# print(int(5428900**0.5))
# print(int(88901**0.5))
