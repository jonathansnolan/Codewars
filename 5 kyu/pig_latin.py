###################################
# QUESTION
###################################

# Move the first letter of each word to the end of it, then add "ay" to the end of the word.
# Leave punctuation marks untouched.

###################################
# SOLUTION
###################################

def pig_it(text):
    x = text.split()
    if text[len(text)-1] == "!":
        x = x[0:len(x)-1]
    elif text[len(text)-1] == "?":
        x = x[0:len(x)-1]

    i = ""
    for k in x:
        i += k[1:] + k[0] + "ay" + " "
    i = i[:(len(i)-1)]

    if text[len(text)-1] == "!":
        i += " !"
    elif text[len(text)-1] == "?":
        i += " ?"
