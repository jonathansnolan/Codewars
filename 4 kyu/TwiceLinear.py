def dbl_linear(n):
    x = list(range(0,n*5))
    i = [1]
    count = 0
    j = 1
    for k in x:
        i.append(2*j+1)
        i.append(3*j+1)
        count += 1
        j = i[count]
    y = sorted(i)
    mylist = list(dict.fromkeys(y))

    return mylist[n]
