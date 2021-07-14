########################################
# QUESTION
########################################
# Write a function that takes in a string of one or more words,
# and returns the same string, but with all five or more letter words
# reversed (Just like the name of this Kata).
# Strings passed in will consist of only letters and spaces.
#  Spaces will be included only when more than one word is present.

# Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
# spinWords( "This is a test") => returns "This is a test"
#  spinWords( "This is another test" )=> returns "This is rehtona test"


###################################
# SOLUTION
###################################

def spin_words(sentence):
    x = sentence.split()

    j = ""
    for k in x:
        if len(k) >= 5:
            j += (k[::-1]) + " "
        else:
            j += k + " "
    j = j[:len(j)-1]
    return j
