########################################
# QUESTION
########################################

# The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

# Examples
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))(("


###################################
# SOLUTION
###################################

def duplicate_encode(word):
    x = list(word.lower())
    u = []
    for k in x:
        if x.count(k) == 1:
            u.append("(")
        elif x.count(k) > 1:
            u.append(")")

    j = ""
    for k in u:
        j += k

    return j
