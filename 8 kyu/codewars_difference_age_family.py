########################################
# QUESTION
########################################

# At the annual family gathering, the family likes to find the oldest
# living family member’s age and the youngest family member’s age and c
# calculate the difference between them.

# You will be given an array of all the family members' ages, in any order.
# The ages will be given in whole numbers, so a baby of 5 months, will have
# an ascribed ‘age’ of 0. Return a new array (a tuple in Python) with
# [youngest age, oldest age, difference between the youngest and oldest age].

###################################
# SOLUTION
###################################


def difference_in_ages(ages):
    x = len(ages)
    ages.sort()
    a = ages[0]
    b = ages[(x-1)]
    c = a - b
    if c>=0:
        c = c
    else:
        c = -c
    z = (a,b,c)
    return z


print(difference_in_ages([16, 22, 31, 44, 3, 38, 27, 41, 88]))
