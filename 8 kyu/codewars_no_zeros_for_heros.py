###################################
# SOLUTION
###################################

def no_boring_zeros(n):

    j = n
    if j <= 0:
        j = -j

    x = list(range(0,100))
    z = []
    for k in x:
        if j/(10**k) != int(j/(10**k)):
            z.append((j/(10**k))*10)

    if n < 0:
        return -max(z)
    if n == 0:
        return 0
    else:
        return max(z)
