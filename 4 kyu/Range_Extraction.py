def solution(args):
    i = []

    ###################################
    # First part is to add the first part of the args list to the i arragy
    ###################################

    # If the first part is not followed by a subsequent number,
    # then you can add it to the array

    if args[0]+1 != args[1]:
        i.append(str(args[0])+",")

    # Else you can add it the array with the string "-" behind it
    elif args[0]+1 == args[1] and args[0]+2 == args[2]:
        i.append(str(args[0])+"-")
    elif args[0]+1 == args[1] and args[0]+2 != args[2]:
        i.append(str(args[0])+",")
    ###################################
    # Part 2
    ###################################
    u = []
    # Next part is to do a loop of it all

    for k in list(range(1,len(args)-1)):
        if k == 0:
            w.append(args[k])
        elif k == len(args):
            w.append(args[k])

        if args[k]+1 != args[k+1] and args[k] -1 != args[k-1]:
            i.append(str(args[k])+",")
        elif args[k]+1 == args[k+1] and args[k] -1 == args[k-1]:
            None
        elif args[k]+1 == args[k+1] and args[k] -1 != args[k-1]:
            u = []
            u.append(args[k])
        if args[k]+1 != args[k+1] and args[k]-1 == args[k-1]:
            u.append((args[k]))
            if len(u) == 1:
                i.append(str(min(u))+",")
            if max(u) - min(u) > 1 and len(u)>1:
                i.append(str(min(u))+"-")
                i.append(str(max(u))+",")
            if max(u)-min(u) == 1:
                i.append(str(min(u))+",")
                i.append(str(max(u))+",")

    if len(u) == 1 and u[0]+1 != args[-1]:
        i.append(str(u[0])+"-")
    elif len(u) == 1 and u[0]+1 == args[-1]:
        i.append(str(u[0])+",")


    i.append(str(args[-1]))
    j = ""
    for k in i:
        j += k
    return j
