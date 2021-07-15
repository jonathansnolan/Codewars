def mix(s1, s2):

    # the following code creates a dictionary called p
    # the keys are the relevant letters
    # the values are the number of times this letters occur in s1

    x = list(s1)
    i = []
    for k in x:
        if k.islower()==True:
            i.append(k)

    i = sorted(i)
    f = list(dict.fromkeys(i))
    p = {}
    for k in f:
        p[k] = i.count(k)

    # now to do the same to s2

    y = list(s2)
    w = []
    for k in y:
        if k.islower()==True:
            w.append(k)

    w = sorted(w)
    n = list(dict.fromkeys(w))
    m = {}
    for k in n:
        m[k] = w.count(k)

    # Now there is two lists: p and m
    # now to make an array listing out the values of each letter
    i = []

    ###########################################
    # Note:
    ###########################################
    # I have just realised that it now needs to also be in order by the word

    for k in p:
        if k in m and p[k]>m[k]:
            i.append("1:"+ p[k]*k)
        elif k not in m and p[k]>1:
            i.append("1:"+ p[k]*k)

    for k in m:
        if k not in p and m[k]>1:
            i.append("2:"+ m[k]*k)
        if k in p and p[k]<m[k]:
            i.append("2:"+ m[k]*k)

    for k in p:
        if k in m and p[k]==m[k] and p[k]>1:
            i.append("=:"+ m[k]*k)



    i = sorted(i, key = len)
    r = []
    for k in i:
        r.append(len(k))
    r = list(dict.fromkeys(r))
    r = r[::-1]

    ans = ""
    for u in r:
        for k in i:
            if len(k) == u:
                ans += k+"/"

    return ans[:-1]
