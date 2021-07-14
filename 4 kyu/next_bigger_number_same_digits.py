from itertools import permutations 

def next_bigger(n):
    x = list(str(n))
    i = []
    for k in x:
        i.append(int(k))
    perm = permutations(i, len(x), )

    p = []
    for i in list(perm):
        l = ""
        for u in i:
            l+= str(u)
        p.append(int(l))
    p = sorted(p)
    p = list(dict.fromkeys(p))


    for k in list(range(0,len(p))):
        if n == p[k]:
            return int(p[k+1])

print(next_bigger(12345313))
