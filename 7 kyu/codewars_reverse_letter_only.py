###################################
# QUESTION
###################################

# Task
# Given a string str, reverse it omitting all non-alphabetic characters.

# Example
# For str = "krishan", the output should be "nahsirk".

# For str = "ultr53o?n", the output should be "nortlu".

# Input/Output
# [input] string str

# A string consists of lowercase latin letters, digits and symbols.

# [output] a string


###################################
# SOLUTION
###################################
def reverse_letter(string):
    x = list(string)
    y = []
    z = ''
    for k in x:
        if k.isalpha() == True:
            y.append(k)
    t = y[::-1]
    for i in t:
        z += i
    return z
