###################################
# QUESTION
###################################

# Given an array of integers.

# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.

# If the input array is empty or null, return an empty array.

# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].


###################################
# SOLUTION
###################################

def count_positives_sum_negatives(arr=''):
    x = len(arr)
    if x == 0:
        return []
    else:
        z = 0
        w = 0
        for k in range(0,x):
            if arr[k] >= 1:
                z += 1
            else:
                w += arr[k]
    return [z,w]
    #your code here
