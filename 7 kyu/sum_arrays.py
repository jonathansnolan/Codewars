def sum_arrays(array1,array2):

    if array1 == [] and array2 ==[]:
        return []
    elif array1 == []:
        return array2
    elif array2 == []:
        return array1
    else:
        x = ''
        y = ''
        for k in array1:
            x += str(k)
        for k in array2:
            y += str(k)

        if  x[0] == "-" and y[0] == "-":
            x = x[1:]
            y = y[1:]
            z = list(str((-int(x)-int(y))))
        elif x[0] == "-":
            x = x[1:]
            z = list(str((-int(x)+int(y))))
        elif y[0] == "-":
            y = y[1:]
            z = list(str((int(x)-int(y))))
        else:
            z = list(str((int(x)+int(y))))

        i = []

        if z[0] == "-":
            z = z[1:]
            for k in z:
                i.append(int(k))
            i[0] = -1*i[0]
            return i
        else:
            for k in z:
                i.append(int(k))
            return i


print(sum_arrays([3,2,6,6],[-7,2,2,8]))
