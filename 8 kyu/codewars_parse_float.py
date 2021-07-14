########################################
# QUESTION
########################################

# Write function parse_float which takes a string/list and returns
# a number or 'none' if conversion is not possible.

#######################################
# SOLUTION
#######################################

def parse_float(string):
    try:
        float(string) >= 0
        return float(string)
    except:
	    return None
