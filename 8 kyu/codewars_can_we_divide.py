########################################
# QUESTION
########################################

# Your task is to create function isDivideBy (or is_divide_by) to check
# if an integer number is divisible by each out of two arguments.

# A few cases:

# (-12, 2, -6)  ->  true
# (-12, 2, -5)  ->  false

# (45, 1, 6)    ->  false
# (45, 5, 15)   ->  true

# (4, 1, 4)     ->  true
# (15, -5, 3)   ->  true

###################################
# SOLUTION
###################################

def is_divide_by(number, a, b):
    if number % a == 0 and number % b == 0:
        return True
    else:
        return False

print(is_divide_by(10, 2, 4))
