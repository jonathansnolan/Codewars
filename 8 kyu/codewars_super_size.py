########################################
# QUESTION
########################################

# Write a function that rearranges an integer into its largest possible value.

# super_size(123456) # 654321
# super_size(105)    # 510
# super_size(12)     # 21

###################################
# SOLUTION
###################################

def super_size(n):
    x = list(str(n))
    z = []
    for k in x:
        z.append(int(k))
    z.sort()
    z = z[::-1]
    y = ''
    for k in z:
        y += str(k)
    y = int(y)
    return y


print(super_size(608719))
