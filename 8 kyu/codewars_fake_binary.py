#######################################
# SOLUTION
#######################################

def fake_bin(s):
    return ''.join('0' if int(c) < 5 else '1' for c in s)
