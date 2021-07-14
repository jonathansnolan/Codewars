########################################
# QUESTION
########################################

# Given a list of numbers, determine whether the sum of its elements is odd or even.

# Give your answer as a string matching "odd" or "even".

# If the input array is empty consider it as: [0] (array with a zero).

###################################
# SOLUTION
###################################



def odd_or_even(arr):
    if sum(arr) % 2 == 0:
        return "even"
    else:
        return "odd"

print(odd_or_even([0,1,3]))
