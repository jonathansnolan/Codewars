def solution(string,markers):
    # first off I want to split the string up
    # by every new line

    x = string.split("\n")
    i = []
    for k in x:
        for u in list(range(0,len(k))):
            if k[u] in markers:
                i.append(k[:u])
                break
        else:
            i.append(k)
    j = ""
    for k in i:
        j += k.strip()+"\n"
    return j[:-1]
