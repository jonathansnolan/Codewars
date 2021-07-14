from collections import Counter

def top_3_words(text):
    text = text.lower()
    count = ""
    j = []
    for u in text:
        if ord(u) > 96 and ord(u) < 123 or ord(u) == 39:
                count += u
        else:
            j.append(count)
            count = ""

    i = []
    for k in j:
        temp = ""
        for u in k:
            if ord(u) > 96 and ord(u) < 123 or ord(u) == 39 and len(k) > 3:
                temp += u
        if temp != "":
            i.append(temp)
    u = dict(Counter(i))
    ans = sorted(u, key=u.get)
    ans = ans[::-1]
    ans = ans[:3]
    return ans
