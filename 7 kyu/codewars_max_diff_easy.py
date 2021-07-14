########################################
# QUESTION
########################################


# You must implement a function maxDiff that return the difference between the biggest and the smallest value in a list(lst) received as parameter.

# The list(lst) contains integers, that means it may contain some negative numbers.

# If the list is empty or contains a single element, return 0.

# The list(lst) is not sorted.

###################################
# SOLUTION
###################################

def max_diff(lst):
    if len(lst) == 1 or lst == []:
        return 0
    else:
        x = min(lst)
        y = max(lst)


        if x >= 0:
            z = y - x
        elif x < 0 and y < 0:
            z = y + x
        else:
            z = y - x
    return z
