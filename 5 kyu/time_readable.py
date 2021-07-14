########################################
# QUESTION
########################################

# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)

# You can find some examples in the test fixtures.

########################################
# SOLUTION
########################################

def make_readable(seconds):
    hours = int(seconds / (60*60))
    mins = int((seconds - hours*60*60)/60)
    sec = (seconds - hours*60*60 - mins*60)

    # THE FOLLOWING CODE MAKES THE NUMBERS 2 DIGITS LONG
    # 1 = 01
    # 4 = 04

    hours = ("%02d" % (hours,))
    mins = ("%02d" % (mins,))
    sec = ("%02d" % (sec,))

    return str(hours) + ":" + str(mins) + ":" + str(sec)
